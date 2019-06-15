import math as m
def dist(a,b):
    return m.sqrt(m.pow((b[0]-a[0]),2)+m.pow((b[1]-a[1]),2))
def SIN(x):
    return m.sin(x*(m.pi/180))
def COS(x):
    return m.cos(x*(m.pi/180))


cam_pos=[[0,0],[50,50],[-50,50]]
cam1=[28.28,28.28]
cam1Angles1=[225,315]
cam2=[76.15]
cam3=[76.15]
cam2Angles2=[246.8]
cam3Angles3=[294]
body_pos1=list()
groups=list()
a=list()
for i in range(len(cam1)):
    a=[]
    x = cam1[i]*COS(cam1Angles1[i])
    y = cam1[i]*SIN(cam1Angles1[i])
    a.append(x)
    a.append(y)
    body_pos1.append(a)
print(body_pos1)
for i in range(len(cam2)):
    a=[]
    x = cam_pos[1][0]+cam2[i]*COS(cam2Angles2[i])
    y = cam_pos[1][1]+cam2[i]*SIN(cam2Angles2[i])
    a.append(x)
    a.append(y)
    body_pos1.append(a)
print(body_pos1)
for i in range(len(cam3)):
    a=[]
    x = cam_pos[2][0]+cam3[i]*COS(cam3Angles3[i])
    y = cam_pos[2][1]+cam3[i]*SIN(cam3Angles3[i])
    a.append(x)
    a.append(y)
    body_pos1.append(a)
print(body_pos1)
for i in range(len(body_pos1)):
    for j in range(len(body_pos1)):
        a=[]
        if(i!=j):
            if(dist(body_pos1[i],body_pos1[j])<=2):
                a.append(body_pos1[i])
                a.append(body_pos1[j])
                groups.append(a)

print(body_pos1)
print(groups)
