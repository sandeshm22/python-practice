import facebook
import os

graph = facebook.GraphAPI(access_token='EAAFzuZAjLpDABAGlzm95UD9ZBcgoKAGmYmkssoUwHyk0JR2YJrFJYKuSPxhMh8UuEYR35AulMUnjreGlHNZCv6WqXI0hN9Pis9V5YaqkAuFrpSLMXe6ORfwUiKR2S4TWCn6lKiCXQ8tBZAcvHM6Oc5Vy29W8igflmQXLKx9gitlGtHUfZAzUPSFjl2Vvjrjrf6dsSTLp6JQZDZD',version = 3.1)
user = graph.request('/me')
userID = user['id']
userPhotosURL = "/"+userID+"/photos/" 
userPhotos = graph.request(userPhotosURL)
#print(friendsList)
#likesData = graph.request("/+" + userID+"/likes")
#print(likesData['data'])

#likes = likesData['data']
#for like in likes:
   #print(like['id'])
   #likeURL = "/" + like['id']
   #likeData = graph.request(likeURL)
   #print(likeData)


for photo in userPhotos['data']:
   #print(photo)
   photoURL = "/" + photo['id'] + "?fields=images"
   photoData = graph.request(photoURL)
   print(photoData)
   xcopyCmd = "xcopy" + photoData['source'] + " ."
   os.system(xcopyCmd)
   

