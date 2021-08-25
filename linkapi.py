import requests
class CombineAPI:
    data1 = ''
    data2 = ''

    # fetching data from both APIs
    def connectapi(self):
        response1 = requests.get("https://my-json-server.typicode.com/typicode/demo/posts")
        print(response1.status_code)
        self.data1 = response1.json()

        response2 = requests.get("https://my-json-server.typicode.com/typicode/demo/comments")
        print(response2.status_code)
        self.data2 = response2.json()

    # adding comments to respective posts.
    def combinedata(self):
        for data in self.data2:
            index = 0
            for post in self.data1:
                if data.get('postId') == post.get('id'):
                    self.data1[index]['comment'] = data.get('body')
                index += 1
        return(self.data1)

ca = CombineAPI()
ca.connectapi()
showdata = ca.combinedata()
print(showdata)