from PIL import Image

#Image conversion
img = Image.open('jerry.JPG')
basewidth = 50
print(img.size)
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img1 = img.resize((basewidth,hsize))
rgb_im = img1.convert('L')
l1=list(rgb_im.getdata())

#Values
small=min(l1)
large=max(l1)
cluster=[]
clusterIndex=[]
cHead=[]
values=[]
k=int(input("enter the no. of clusters"))

#Cluster Head
for i in range(k):
    cHead.append(small+i*large/k)
    values.append(int(small+i*large/k))
    cluster.append([])
    clusterIndex.append([])

5#Appending the values inside the clusters
def clusterForm(i,index,c1uster,clusterIndex):
    b=[]    
    for j in range(k):
        b.append(abs(cHead[j]-i))
    c1uster[b.index(min(b))].append(i)
    clusterIndex[b.index(min(b))].append(index)

#Creating new cluster head for recursion
def createHead(sum1,cluster):
        for i in cluster:
            sum1.append(sum(i)/len(i))
        return sum1

#Kmeans to create clusters           
def kmean(l1, cHead, k,c1uster,clusterIndex):
    sum1=[] #This will be the new cluster head

    #Clearing the old values inside the cluster and index list
    for i in range(k):
        c1uster[i].clear()
        clusterIndex[i].clear()

    for i in range(len(l1)):
        clusterForm(l1[i],i,c1uster,clusterIndex)

    sum1=createHead(sum1,cluster)

    count=0
    for i in range(k):
        if(cHead[i]==sum1[i]):
            count+=1

    if(count!=k): #If old cluster head and new cluster head are same stop the recursion
        kmean(l1,sum1,k,c1uster,clusterIndex)

     
kmean(l1,cHead,k,cluster,clusterIndex) #initial calling of the kmean function

#New colour values inside new image
for i in range(len(clusterIndex)):
    for j in range(len(clusterIndex[i])):
        l1[clusterIndex[i][j]]=values[i]

#Creating a new image                   
im2 = Image.new('L',(basewidth,hsize))

#inserting the new colour value list in the image
im2.putdata(l1)
im2.show()           


  
