import os
import re
files = [f for f in os.listdir() if os.path.isfile(f) & f.endswith('.out')]

l = []

for file in files:
   #print(file) 
   f = open(file, 'r')
   txt = f.read().split('config-only to output data dir')
   for bl in txt:
      a = []
      scs = re.findall('number of scf cycles\s+\=\s+([0-9]+)', bl)
      for scf in scs:
         a.append(scf)
      es = re.findall('enthalpy\s+new\s+\=\s+(\-?[0-9]+\.[0-9]+)\sRy', bl)
      for enthalpy in es:
         a.append(enthalpy)
      vs = re.findall('new unit\-cell volume\s+\=.+\s+([0-9]+\.[0-9]+)\sAng\^3\s\)', bl)
      for vol in vs:
         a.append(vol)
      ds = re.findall('density\s+\=\s+([0-9]+\.[0-9]+)\sg\/', bl)
      for density in ds:
         a.append(density)
      cpus = re.findall('total cpu time spent up to now is\s+([0-9]+\.[0-9]+)\ssecs', bl)
      #cpus.reverse()
      first = 0
      total = 0
      count = 0
      for cpu in cpus:
         if count == 0: first = float(cpu)
         total = float(cpu)
         count +=1
      a.append(count)
      a.append( round((total-first)/3600, 1) )
      if scs: 
         #print(a)
         l.append(a)
   f.close()


l.insert(0, ['SCF steps','Enthalpy (Ry)','Volume (Ang^3)','Density (g/cm^3)','SCF Interations','CPU Time (h)'])
with open('OUTPUT_extract_data_outputfile.txt', 'w') as o:
  for i in l:
        print("{};{};{};{};{};{}".format(i[0], i[1], i[2], i[3], i[4], i[5]), file=o)


