import os
from subprocess import *

from rest_framework.response import Response
from rest_framework.views import APIView

from helper import *
import json
from django.http import HttpResponse, JsonResponse

class CliView(APIView):
    """Pass in command directly to sherlock."""
    def post(self, request):
        data = json.loads(request.body)
        user = data['user']
        args = data['args']
        # print(f"`{user}`") 
        # print(f"`{args}`")

        try:
            if valid_args(args) == False or valid_args(user) == False or not user or not args:
                return JsonResponse({})
            else:
                full_cmd = f"{py_command()} {sherlock_dir()}/maigret.py {user} {args} --json simple"
                proc = Popen(full_cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
                proc.communicate()
        except:
            print("ERR1")
            return JsonResponse({})

        try:
            with open(f"reports/report_{user}_simple.json", 'r') as f:
                report = json.load(f)

            output = {
                "Username": user
            }

            accounts = []
            interests = set()
            for i in report:
                k = i
                if k == "GitHubGist":
                    k = "GitHub"
                if k == "Nitter":
                    k = "Twitter"
                if k == "Pixwox":
                    k = "Instagram"

                accounts.append({
                    "Name": k,
                    "URL": report[i].get("url_user", "").
                        replace("https://nitter.net/", "https://twitter.com/").
                        replace("https://gist.github.com/", "https://github.com/").
                        replace("https://www.pixwox.com/profile/", "https://www.instagram.com/"),
                })
                for j in report[i].get("site", []).get("tags", []):
                    if j != "us":
                        interests.add(j)
            output["Interests"] = ", ".join(interests)
            output["Accounts"] = accounts

            return JsonResponse(output)
        except Exception as e:
            print("ERR2", e)
            return JsonResponse({})

class DataView(APIView):
    """Request JSON data from sherlock resources."""
    def get(self, request):
        return Response(sherlock_data())
