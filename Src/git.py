from github import Github
import base64

print("########################################################################")
print("                        GITHUB CLI SERCHER")
print("########################################################################")
print("Available commands:")
print("1-Search all the user public repos")
print("2-Search a specific repo")
print("3-Search a specific language or topic")

select_command = int(input())
def searchuRepo():
    print("Enter yuor or another username from github")
    selecUserename = input()
    g = Github()
    user = g.get_user(selecUserename)
    def print_repo(repo):
        # repository full name
        print("Full name:", repo.full_name)
        # repository description
        print("Description:", repo.description)
        # the date of when the repo was created
        print("Date created:", repo.created_at)
        # the date of the last git push
        print("Date of last push:", repo.pushed_at)
        # home website (if available)
        print("Home Page:", repo.homepage)
        # programming language
        print("Language:", repo.language)
        # number of forks
        print("Number of forks:", repo.forks)
        # number of stars
        print("Number of stars:", repo.stargazers_count)
        print("-"*50)
        # repository content (files & directories)
        print("Contents:")
        for content in repo.get_contents(""):
            print(content)
        try:
            # repo license
            print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
        except:
            pass
    for repo in user.get_repos():
        print_repo(repo)
        print("="*100)
def searchpRepo(): 
    print("Insert the query!")
    query = input()
    g = Github()
    def prints_repo(repo):
        # repository full name
        print("Full name:", repo.full_name)
        # repository description
        print("Description:", repo.description)
        # the date of when the repo was created
        print("Date created:", repo.created_at)
        # the date of the last git push
        print("Date of last push:", repo.pushed_at)
        # home website (if available)
        print("Home Page:", repo.homepage)
        # programming language
        print("Language:", repo.language)
        # number of forks
        print("Number of forks:", repo.forks)
        # number of stars
        print("Number of stars:", repo.stargazers_count)
        print("-"*50)
        # repository content (files & directories)
        print("Contents:")
        for content in repo.get_contents(""):
            print(content)
        try:
            # repo license
            print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
        except:
            pass
    for repo in g.search_repositories(query):
        prints_repo(repo)
def serchtRepo():
    print("The language/topic, followed by a colons, and the language and topic")
    print("eg: language: python/ topic: machine-learning")
    tselect = input()
    g = Github()
    def printt_repo(repo):
        # repository full name
        print("Full name:", repo.full_name)
        # repository description
        print("Description:", repo.description)
        # the date of when the repo was created
        print("Date created:", repo.created_at)
        # the date of the last git push
        print("Date of last push:", repo.pushed_at)
        # home website (if available)
        print("Home Page:", repo.homepage)
        # programming language
        print("Language:", repo.language)
        # number of forks
        print("Number of forks:", repo.forks)
        # number of stars
        print("Number of stars:", repo.stargazers_count)
        print("-"*50)
        # repository content (files & directories)
        print("Contents:")
        for content in repo.get_contents(""):
            print(content)
        try:
            # repo license
            print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
        except:
            pass
    for i, repo in enumerate(g.search_repositories(tselect)):
        printt_repo(repo)
        print("="*100)
        if i == 9:
            break
if select_command == 1:
    searchuRepo()
elif select_command == 2:
    searchpRepo()
elif select_command == 3:
    serchtRepo()
