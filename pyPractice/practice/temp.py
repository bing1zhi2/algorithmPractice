"""
void tffun(const double* in, double* out){
    double alpha,beta
    if(in[0] == 0.0 && in[1] == 0.0){
        if(in[2] > 0)
        alpha = 0
        else
        alpha = -M_PI
    }else{
        alpha = acos(in[0]/sqrt(in[0]*in[0]+in[1]*in[1]))
    }

    beta = acos(in[2]/sqrt(in[0]*in[0]+in[1]*in[1]+in[2]*in[2]))

    double r11,r12,r13,r21,r22,r23,r31,r32,r33
    r11 = cos(alpha)*cos(beta)
    r12 = -sin(alpha)
    r13 = cos(alpha)*sin(beta)

    r21 = sin(alpha)*cos(beta)
    r22 = cos(alpha)
    r23 = sin(alpha)*sin(beta)

    r31 = -sin(beta)
    r32 = 0
    r33 = cos(beta)

    double theta = acos((r11+r22+r33-1)/2)

    out[0] = 1/(2*sin(theta))*(r32-r23)*theta
    out[1] = 1/(2*sin(theta))*(r13-r31)*theta
    out[2] = 1/(2*sin(theta))*(r21-r12)*theta
}
"""
import math
from math import cos as cos, sin as sin, acos as acos, cos as cos


def tffun(input_arr):
    output_arr = []
    alpha = 0.0
    beta = 0.0

    if input_arr[0] == 0 and input_arr[1] == 0:
        if input_arr[2] > 0:
            alpha = 0.0
        else:
            alpha = - math.pi
    else:
        alpha = acos(input_arr[0]/math.sqrt(input_arr[0]*input_arr[0]+input_arr[1]*input_arr[1]))

    asum = math.sqrt(input_arr[0]*input_arr[0] + input_arr[1]*input_arr[1]+input_arr[2]*input_arr[2])
    beta = acos(input_arr[2]/asum)

    r11=cos(alpha)*cos(beta)
    r12=-sin(alpha)
    r13=cos(alpha)*sin(beta)

    r21=sin(alpha)*cos(beta)
    r22=cos(alpha)
    r23=sin(alpha)*sin(beta)

    r31=-sin(beta)
    r32=0
    r33=cos(beta)

    theta=acos((r11+r22+r33-1)/2)

    out=[0.0, 0.0, 0.0]

    out[0]=1/(2*sin(theta))*(r32-r23)*theta
    out[1]=1/(2*sin(theta))*(r13-r31)*theta
    out[2]=1/(2*sin(theta))*(r21-r12)*theta

    return out



input_arr=[1, 3, 4, 5]

out_arr=tffun(input_arr)
print(out_arr)
