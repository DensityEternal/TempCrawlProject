import random
import re
import time

import requests
from bs4 import BeautifulSoup


def WeLearn(n) -> int:
    headers = {
        'cookie': 'acw_tc=2760825216976342495825606e7698020bcedccb9ff0d55aafbce0db929997; ASP.NET_SessionId=1xaxdow2fc5i005fni0bxkjk; .AspNet.Cookies=WIqjUT_dwcLvWEaYTr7dmQVLLvhbTq6Lq62xV2w0x1jaTPUuQzDw8N8ETqi6T_UfgBfAyLB2P85SQNpQk3_pYYNREBkig-cCRZ2viSmkNsfe6jKqa7rbwIKZBnm9ZM6QRR2ZGb3Jd9cOn2LHv6eoNhl67nS7alQH6Mogw9ocKkai1XPskOlEPnyrw8sf2VsOQdtpF-ej2dCjanAN3YK6TH-oMuWGYPJLxQxjHeaHzZLqMaaqYHQveYbDKFWtSQ52q3xrWQ37Z__8B5XONn4JCbdUQEC9AEKv4ss2GinywFSSJw8SJ3FdXU-am_LpXq9VRxnfzIpnpA4Vdb2RQ0OZYOXD2UyVPFvVxD8edzBuGpq-ypgvfbktw67DuygfLPB8QRjs9zmrWtnx_NDGmSNZ9dnOGEJVRPKqX9WNTsupqL0w1Mi8OaGBSePXzhmbuEggvX-gOwRs8EK78eE5xndKJVW1qoGYCTiACurhjigs-v5b1e6PURA1__7-gQ9llKL6MtBNSCPCpZAIH1YtyvXpJRbvzcuhOm4NrQaw1K6rQIVSYAvvZfL5a3fyNSvIjSgN9uIjKNmCsxcWtK0ZqfLjsLKK-xybWmHM0fdafcngsJm4uS8B1Gt8rDL5imuhlEOKHwBxjkmFpVVm4M0k1iMQSprY2qaJv9NVOyWJ_CWYFKV1fIGXCyLHe1xUOKuY9tJaeHXw1US8DdLvayHWpC__j8_ooPLZVAshF_ffjPN6h7npvAodz0Zg5hHCHQ02MFNc4qb9WrbZW4VjS94x6xsw5zi_o-B1OjJXDCyuS6YH_kGpAfHbZm00w1LqFh82cpsYcrIWIBY1y-h_DuU6hqHucZHVkMzT1CotrAqPskMpQASak-nB4wmyPGQ_5z31InOnBiZYdCEBlh9RmkttdDULL294nIc5ukuUE3Je_L6CpJSE53OvOlSMSvC88MSvdTO_Fj_JdQ_VwQcyglxFeZ-rNIFp4sB6gqy0y8kfAQj_z6i6hOZWLDWdr_2mrSK6bSlBQ8tEAPF57N6ZhURTv4AKrZXgLpN670YYSSsJKps5k86l1gHkWyiS7fmVOK0psQySOtwx-4UjJshBOdfZGMaBX6QL1HDZuhGVD2NjZw6Do81GWnR-dOfRXdIpQ9gLxLj5hQEBpE-96w4tRzSasedkUspN7kn8oto6ucN_4Q299xjyMYvDmNZhPL4WS8ISQ4pIVTJeRgblXi-QReqgtgJDPZu5sOV2UvkDlv0ia-uyyC3kM7EcOu9s75Igfcv6nqdxKYgJJJmKINU9nKG04BG_tubdEbZeNYaBSTtsTCC-SelHfD_kbUFB2onwODlM1BmcDEk-DOicgE4kuZYIhOp9_bdUhiuG55ZVK5E6aKXtNUWvN9zeKK1mM975tnyvKdzXwv82RDQvdidEFlkU_IiiN6WeSl_3YpaiE52nTG1p-yCT9w3o6xcfmLU6akZRFHMyh5nlBt_CIv6L3jrB-_FprgXim6xOGZ77XrdQA7jlIz951_3X43BIBftoOuVZPESP-0GlWRMMH0rZa0Hw65VtpWXG_vY7Kf8ct--Kw6Lq4fBjjTqXGTSV7yBmf4XOkUk3W-eRIYoOe5wyykRVXs3FrfbGtyKq3dm6NTUYRF5dhwpgv581yek_5b0G11GaRLJYkiPWriDrq1-pdVHeKlUU_GizEbn8enOmG_4ZodcfY6ilFqjoFD0guHZiNUAJzmR5XW9zSKvHOWQfkyaawAdu0pqdKUW1gO-UBdH1uJ3zjaYAl8CrbrngRGGrKa4gb-nXgL0Wcdh8q5QQY6i-8L68C8U595TwdLX383NhMGlJshjoJuz1rX6DagJ3plFP-Y_e1KnTpsZ2PLetnR_tN59Xkj0RewjbpYCLlZuejNX-NjC8JYet9b14TXcVzxmqfJM_x0mx9JIL4G6F4DDEn0Z5BVFcd2unRNNrtEKRnz9dGYLug4Kp1EvodyFy-NVY87J-RoDNJGkfNeKHSTZekiacA4yRI406TzScPnQgct9W1nGvqL8EF0D2KQtupNHo525zm2BqvvGZwV0jtYELy9FoMngo2-zz9T1j4dO-gAYAVblFVIH4BRLoA7xytE4rVPVk0zoKNSQpd8rPxA3Nl88e6bd1G9rpH7oLtvB41ZYS7AtUQr1sxHIaIfRCnH4PBUbamVkH4kr6JJcChYmRB0EtHxWg_IV4BP_uO8g9WCA6jyKSTQ5SWjsYd5Cfky6vROyac0NDXXrUDaVg2xTm6rIwyd8MzeDULL89AOemQdIKaI_y-WxxYob7uijq0n-pHnhaK0iefH6KdoOitm1eHbxIsk1t9p3uiUvOrO_IzlMk7uQqezeSk5h3q6EyNpWpNRcMgtpkiGQxrojHa6wRH7iQ2ZxKTKQ_njT_cVyjufgm9jI_ugxsqHVw_M2OOuuDFULjRgiyI7ofUdWjCAafIdfGC_SV0PjwWERHniCeb9-6wprYm41BsqpSH-zdy0ZE31x3f2ffiodYk-PGqSp0_hlh0YcOFH41q3oeiHVwZfH0ntBU8XX07Ih0Vgc8pKF-_tY_QmYM5c8afpcRca6-nEk-FQqKuyRaSXRzykw2Zh-y9dznRokq7F9rKcTfz6rlP-dG1Zw8IvfnWwZbpvAhTl9EQyp2rxEd4prX5InNLBUJfzO38M7IzDHNwMpj8a3qnSb1gOgq7onTsre-LwDli-zHeztW0j6HYqv648eWeoU6SEocpJswVntpfj_FafdihHW7Cn6rYx_1XmQaEKJe7OFV2zIFGAVrpt9pauJfJL1Qk3UTeh0gelT3ddIUAKy1TfZQ60OAqe11vASBDduPqtD1TQ; area=master; _ga=GA1.2.2097619690.1697634276; _gid=GA1.2.349188108.1697634276; _gat=1; _ga_PNJRS2N8S4=GS1.2.1697634276.1.1.1697634282.0.0.0'

    }

    TargetUrl = []

    for i in range(1, 30):
        TargetUrl.append(
            f'https://centercourseware.sflep.com/Pioneer%20College%20English%20Integrated%20Course%201/unit_0{n}/main{i}.html?m-1-{n}-{i}&nocache=' + str(
                random.random()))
        time.sleep(0.1)
    i = 1
    for url in TargetUrl:
        # print(url)
        response = requests.get(url, headers=headers)

        pattern = re.compile('data-solution="(.*?)"')

        ans = pattern.findall(response.text)

        has_empty_string = sum(len(item) for item in ans)
        # print(has_empty_string)
        filename = f'm-1-{n}-{i}'
        i += 1

        if not has_empty_string:
            try:
                tx = BeautifulSoup(response.content, 'html.parser').findAll('li', {'data-solution': True})
                empty = sum(len(item) for item in tx)
                # print(empty)
                if empty:
                    with open(f'AnswerTest/{filename}.txt', 'w', encoding='utf-8') as file:
                        for x in tx:
                            try:

                                file.writelines(''.join(x.text.split()[0]))
                                file.writelines("\n")
                            except:
                                print(filename, end='')
                                print("不需要写答案")


                else:
                    tx = BeautifulSoup(response.content, 'html.parser').findAll('div', {'data-itemtype': 'result'})

                    for x in tx:
                        with open(f'AnswerTest/{filename}.txt', 'w', encoding='utf-8') as file:
                            try:
                                # print("开始尝试第二部分")
                                file.writelines('\n'.join(x.text))
                            except:
                                print(filename, end='')
                                print("不需要写答案")

            except:
                pass

        else:
            try:
                with open(f'AnswerTest/{filename}.txt', 'w', encoding='utf-8') as file:
                    file.writelines('\n'.join(ans))
            except:
                print(filename, end='')
                print("不需要写答案")
if __name__=="__main__":
    WeLearn()