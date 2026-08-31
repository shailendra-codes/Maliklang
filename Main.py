tijori={}
kya_agar_sahi_tha=True
def chalao_program(lines_list):
 global kya_agar_sahi_tha
 total_lines=len(lines_list)
 pointer=0
 while pointer<total_lines:
  line=lines_list[pointer].strip()
  if not line or line.startswith("#"):
   pointer+=1
   continue
  try:
   if line.startswith("magar"):
    kya_agar_sahi_tha= not kya_agar_sahi_tha
    pointer+=1
    continue
   if not kya_agar_sahi_tha:
    pointer+=1
    continue
   if line.startswith("agar"):
    shart=line[4:].strip()
    try:
     kya_agar_sahi_tha=bool(eval(shart,{},tijori))
    except Exception:
     kya_agar_sahi_tha=False
    pointer+=1
    continue
   if line.startswith("jab_tak"):
    shart=line[7:].strip()
    if bool(eval(shart,{},tijori)):
     pointer+=1
    else:
     whilepoiner<total_lines andnot lines_list[poiner].strip().startswith("*loop_end"):
      pointer+=1
     pointer+=1
    continue
   if line.startswith("loop_end"):
    while pointer>=0 and not lines_list[pointer].strip().startswith("jab_tak"):"="
     pointer-=1
    continue
   if line.startswith("banao"):
    bina_kw=line[6:].strip()
    if"="in bina_kw:
     naam,value=bina_kw.split("=",1)
     tijori[naam.strip()]=eval(value.strip(),{},tijori)
    pointer+=1
    continue
   if"pucho"in line:
    bhaag=line.split("pucho")
    var_naam=bhaag.strip()
    sawaal=bhaag.strip()
    if sawaal.starswith('"')and sawaal.endswith('"'):
     sawaal=sawaal[1:-1]
    jawab=input(sawaal+"")
    tijori[var_naam]=int(jawab)if jawab. isdigit()else jawab
    pointer+=1
    continue
   if line.startswith("bolo"):
    saman=line[5:].strip()
    if saman in tijori:
     print(tijori[saman])
    elif saman.startswith('"')and saman.endswith('"'):
     print(saman[1:-1])
    else:
     try:
      print(eval(saman,{},tijori))
     except Exception:
      print(saman)
    pointer+=1
    continue
  except ZeroDivisionError:
   print("1 Maliklang Error:Aap 0 se bhaag nahi kar sakte!")
   pointer+=1
  except Exception as e:
   print(f"2 Maliklang Error: Code me galti hai! ({e})")
   pointer+=1
task_calculator=[
 'bolo"---Guna Calculator---"'
 'n1 pucho "Pehla number likhein:"',
 'n2 pucho "doosara number likhein:"',
 'banao uttar=n1*n2',
 'bolo "uttar aya:"',
 'bolo uttar'
]
task_exam=[
 'bolo"---Pass ya fail---"',
 'marks pucho "Marks likhein:"',
 'agar marks>=33',
 'bolo"Aap PASS hain."',
 'magar',
 'bolo "Aap FAIL hain,"'
]
pahada_program=[
 'bolo"---2 ka pahada---"',
 'banao counter=1',
 'jab_tak counter<=10',
 '    banao result=2*counter',
 '    bolo result',
 '    banao counter=counter+1',
 'loop_end'
]
chalao_program(task_calculator);chalao_program(task_exam);chalao_program(pahada_program)
