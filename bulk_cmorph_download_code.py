import requests
import numpy as np
import os

years = np.arange(1998,2021)
months = np.arange(1,13)
days_fs = np.arange(1,29)
odds = np.arange(1,32)
evens = np.arange(1,31)

for year in years:
    os.mkdir(r'C:\Users\Okram\Desktop\py\ ' + str(year)) #change your path
    for month in months:
        os.mkdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month))
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////        
        if month == 2: # Febry
            for day in days_fs:
                if day <=9:
                    os.chdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month)+'\ ')#change your path
                    url_1 = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+str(year)+'/'+'0'+str(month)+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+ str(year)+'0'+str(month)+'0'+str(day)+'.nc'    
                    r = requests.get(url_1, allow_redirects = True)
                    open(str(year)+'0'+str(month)+'0'+str(day)+'.nc','wb').write(r.content)
                elif day >=10:
                    os.chdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month)+'\ ') #change your path
                    url_2 = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+str(year)+'/'+'0'+str(month)+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+ str(year)+'0'+str(month)+str(day)+'.nc'     
                    r = requests.get(url_2, allow_redirects = True)
                    open(str(year)+'0'+str(month)+str(day)+'.nc','wb').write(r.content)
 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\       
        if month%2==0 and month !=2:# Even months
            if month <=9:
                for even in evens:
                    if even <=9:
                        os.chdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month)+'\ ') #change your path
                        url_3 = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+str(year)+'/'+'0'+str(month)+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+ str(year)+'0'+str(month)+'0'+str(even)+'.nc'    
                        r = requests.get(url_3, allow_redirects = True)
                        open(str(year)+'0'+str(month)+'0'+str(even)+'.nc','wb').write(r.content)
                    elif even>=10:
                        os.chdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month)+'\ ') #change your path
                        url_4 = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+str(year)+'/'+'0'+str(month)+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+str(year)+'0'+str(month)+str(even)+'.nc'    
                        r = requests.get(url_4, allow_redirects = True)
                        open(str(year)+'0'+str(month)+str(even)+'.nc','wb').write(r.content)
            if month >=10 and month <=31:
               for even in evens:
                    if even<=9:
                        os.chdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month)+'\ ') #change your path
                        url_5 = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+str(year)+'/'+str(month)+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+ str(year)+str(month)+'0'+str(even)+'.nc'     
                        r = requests.get(url_5, allow_redirects = True)
                        open(str(year)+str(month)+'0'+str(even)+'.nc','wb').write(r.content)
                    elif even>=10:
                        os.chdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month)+'\ ') #change your path
                        url_6 = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+str(year)+'/'+str(month)+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+str(year)+str(month)+str(even)+'.nc'    
                        r = requests.get(url_6, allow_redirects = True)
                        open(str(year)+str(month)+str(even)+'.nc','wb').write(r.content)
                 
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 
                        
        if month%2!=0 and month !=2: # odd months
            if month <=9 :
                for odd in odds:
                    if odd<=9:
                        os.chdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month)+'\ ') #change your path
                        url_5 = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+str(year)+'/'+'0'+str(month)+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+ str(year)+'0'+str(month)+'0'+str(odd)+'.nc'     
                        r = requests.get(url_5, allow_redirects = True)
                        open(str(year)+'0'+str(month)+'0'+str(odd)+'.nc','wb').write(r.content)
                    elif odd>=10:
                        os.chdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month)+'\ ') #change your path
                        url_6 = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+str(year)+'/'+'0'+str(month)+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+str(year)+'0'+str(month)+str(odd)+'.nc'    
                        r = requests.get(url_6, allow_redirects = True)
                        open(str(year)+'0'+str(month)+str(odd)+'.nc','wb').write(r.content)
            if month >=10 and month <=31: 
                 for odd in odds:
                    if odd<=9:
                        os.chdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month)+'\ ') #change your path
                        url_5 = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+str(year)+'/'+ str(month)+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+ str(year)+str(month)+'0'+str(odd)+'.nc'     
                        r = requests.get(url_5, allow_redirects = True)
                        open(str(year)+str(month)+'0'+str(odd)+'.nc','wb').write(r.content)
                    elif odd>=10:
                        os.chdir(r'C:\Users\Okram\Desktop\py\ '+str(year)+'\ ' +str(month)+'\ ') #change your path
                        url_6 = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+str(year)+'/'+str(month)+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+str(year)+str(month)+str(odd)+'.nc'    
                        r = requests.get(url_6, allow_redirects = True)
                        open(str(year)+str(month)+str(odd)+'.nc','wb').write(r.content)
                 
