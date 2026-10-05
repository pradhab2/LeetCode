class trie():
    head={}
    def add(self,word):
        curr=self.head
        for chr in word:
            if chr not in curr:
                curr[chr]={}
            curr=curr[chr]
        curr['*']=True

    def search(self,word):
        curr=self.head
        for chr in word:
            if chr not in curr:
                return False
            curr=curr[chr]
        if curr['*'] != True:
            return False
        return True

tr=trie()
tr.add('hello')
tr.add('hey')
tr.add('he')
tr.add('m')

print("Trie DS is: %s" % tr.head)
print(tr.search('hello'))

print(tr.search('heyu'))
