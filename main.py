import asyncio
from crossref.restful import Works, Journals


async def main():
    # journals = Journals()
    # try:
    #     async for item in await journals.all():
    #         print(item["ISSN"])
    #         print(item["title"])
    #         print(item["publisher"])
    # except Exception as e:
    #     pass
    works = Works()
    # aa = await works.doi("10.1016/S0140-6736(97)11096-0")
    # print(aa)
    async for i in await works.filter(from_pub_date='2016'):
        if "reference-count" in i.keys():
            print("reference-count:", i["reference-count"])
        if "publisher" in i.keys():
            print("publisher:", i["publisher"])
        if "issue" in i.keys():
            print("issue:", i["issue"])
        if "DOI" in i.keys():
            print("DOI:", i["DOI"])
        if "type" in i.keys():
            print("type:", i["type"])
        if "page" in i.keys():
            print("page:", i["page"])
        if "source" in i.keys():
            print("source:", i["source"])
        # if "author" in i.keys():
        #     print("author:", i["author"])
        # if "reference" in i.keys():
        #     print("reference:", i["reference"])
        if "URL" in i.keys():
            print("URL:", i["URL"])
        if "ISSN" in i.keys():
            print("ISSN:", i["ISSN"])
        if "subject" in i.keys():
            print("subject:", i["subject"])
        print("keys:", i.keys())
asyncio.run(main())
