import discord
import asyncio
import random

client = discord.Client()

token = "NTcxNTk2MTUxMDAyNzU5MTg5.XMQCkQ.MBVruSm8mkb-mPoZ8wL0ToiEKg0"

@client.event
async def on_ready():
    print("Login as: ")
    print(client.user.name)
    print(client.user.id)
    print("===============")
    await client.change_presence(game=discord.Game(name='ㅎㅇ',type=1))

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    channel = message.channel
    id = message.author.id
    if message.content.startswith('!커맨드'):
        await client.send_message(channel,'커맨드')

    if message.content.startswith('!안녕'):
        await client.send_message(channel,'안녕')

    if message.content.startswith('!제조'):
        a = random.randint(1,100000)
        if a==100000:
            string = "댁안이 캠키고 태보20분시키기 이용권"
        if a==99999:
            string = "댁안이 코스프레 이용권(비용은 반반씩)"
        if a != 100000 and a != 99999:
            list = ['IDW','제리코','스테츠킨','K5','컨텐더','Px4스톰','캘리코','그리즐리','PA-15','MP7','100식','츤','P90','G36C','포돌이','(기하와)벡터','리베롤','M14','G36','9A-91','FAL','과탑','중자매','K2','AN-94♥','댕댕이','흥구기','라플비', '자스','마일리','춘전이','스브드','M200','포도카노','Kar98k','딸기카노','NTW-20','M99','IWS2000','브렌','M2HB','M1918','Mk-48','PK','88식','네게브','MG36','MG4','MG5','PKP','SPAS-12','USAS-12','KSG','Sagia-12','S.A.T.8','AA-12']
            string = random.choice(list)
        await client.send_message(channel,"<@"+id+"> 님이"+string+"을(를) 제조하였습니다.")

    if message.content.startswith("!정보"):
        if "콜트리볼버" in message.content or"콜트 리볼버" in message.content or "콜라" in message.content or "00:50" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "콜트 리볼버(성우:타나카 아이미,일러스트:Saru)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:50",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n■ ● ■\n□ ■ □\n버프칸의 모든총기에게 화력24%, 명중50%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**일제사격**\n아군 전체 화력을 22% 상승시킨다. 지속시간 8초",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/1.png")
            await client.send_message(channel,embed=embed)

        elif "M1911" in message.content or"m1911" in message.content or "운메이" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M1911(성우:마츠이 에리코,일러스트:Spirtie)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:50",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n■ ● ■\n□ ■ □\n버프칸의 모든총기에게 사속 20%, 명중 50%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**연막탄**\n폭발한 위치의 2.5 반경에 적의 사속/이속을 감소시키는 연막이 발생",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/2.png")    
            await client.send_message(channel,embed=embed)

        elif "M9" in message.content or"m9" in message.content or "엠구" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M9(성우:스자키 아야,일러스트:M. vv)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ ■\n□ ● □\n□ ■ ■\n버프칸의 모든총기에게 화력 20%, 회피 20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**섬광탄**\n폭발한 위치의 2.5 내의 적에게 기절을 건다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/3.png")    
            await client.send_message(channel,embed=embed)

        elif "콜트 파이슨" in message.content or"콜트파이슨" in message.content or "파이슨" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "콜트 파이슨(성우:읍읍읍,일러스트:REALMBW)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ ■\n■ ● ■\n■ ■ □\n버프칸의 모든총기에게 화력 30%, 치명타율 20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**겁없는 녀석들**\n패시브: 자신이 화력 / 사속 / 회피 / 명중 / 치명타율 버프를 받을 때(요정특성 포함)버프 진형의 아군에게 해당 스탯 버프 부여(3초 지속, 최대 3중첩)\n액티브: 발동 후 6회의 공격은 일정 확률로 지속시간 동안 자신의 화력 상승(최대 6중첩)",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/4.png")    
            await client.send_message(channel,embed=embed)        

        elif "나강 리볼버" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "나강 리볼버(성우:시노하라 나루미,일러스트:X布)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:20",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n■ ● □\n□ ■ □\n버프칸의 모든총기에게 화력 32%, 치명타율 16%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**기선제압N**\n지속시간 동안 적 전체 화력 감소",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/5.png")    
            await client.send_message(channel,embed=embed)

        elif "토카레프" in message.content or "토카" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "토카레프(성우:사쿠마 히로미,일러스트:废人)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:45",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ ■\n□ ● □\n□ ■ ■\n버프칸의 모든총기에게 사속 20%, 명중 50%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**엄호개시**\n지속시간 동안 아군 전체 회피 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/6.png")    
            await client.send_message(channel,embed=embed)    
    
        elif "스테츠킨" in message.content or "수제치킨" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "스테츠킨(성우:키타무라 에리,일러스트:鳗鱼子)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:55",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ ■\n□ ● □\n□ ■ ■\n버프칸의 모든총기에게 화력 12%, 사속 24%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**진압신호**\n지속시간 동안 아군 전원 사속 상승",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/7.png")    
            await client.send_message(channel,embed=embed)  

        elif "마카로프" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "마카로프(성우:우에사카 스미레,일러스트:河马)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● ■\n■ □ □\n버프칸의 모든총기에게 화력 20%, 사속 12%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**시야봉쇄**\n지속시간 동안 적 전체 명중 감소",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/8.png")    
            await client.send_message(channel,embed=embed)    

        elif "p38" in message.content or "피38" in message.content or "P38" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "P38(성우:카나에 토오루,일러스트:とり)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:20",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ ■\n□ ● □\n□ ■ ■\n버프칸의 모든총기에게 사속 14%, 명중 56%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**조명탄**\n지속시간 동안 아군 전체 명중 상승(야간작전 전용)",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/9.png")
            await client.send_message(channel,embed=embed)   

        elif "ppk" in message.content or "PPK" in message.content or "지휘를좀더대국적으로하십시오" in message.content :
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "PPK(성우:이토 아스카,일러스트:堀森)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:22",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● ■\n■ □ □\n버프칸의 모든총기에게 사속 32%, 치명률 16%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**사냥신호**\n지속시간 동안 아군 전원 화력,치명률 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/10.png")    
            await client.send_message(channel,embed=embed)   

        elif "p08" in message.content or "P08" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "P08(성우:우에사카 스미레,일러스트:河马)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● ■\n□ ■ □\n버프칸의 모든총기에게 화력 14%, 명중 70%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**엄호개시N**\n지속시간 동안 아군 전체 회피 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/11.png")    
            await client.send_message(channel,embed=embed)

        elif "c96" in message.content or "C96" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "C96(성우:이타타니 아야카,일러스트:林檎爱す)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n□ ● ■\n■ □ □\n버프칸의 모든총기에게 화력 14%, 명중 70%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**조명탄**\n지속시간 동안 아군 전체 명중 증가(야간작전 전용)",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/12.png")    
            await client.send_message(channel,embed=embed) 

        elif "92식" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "92식(성우:미모리 스즈코,일러스트:莲子)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:35",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ ■ ■\n■ ● ■\n■ ■ ■\n버프칸의 모든총기에게 명중 50%, 회피 40%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**돌격개시**\n지속시간 동안 아군 전체 화력,사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/13.png")    
            await client.send_message(channel,embed=embed)

        elif "아스트라 리볼버" in message.content or "아스트라" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "아스트라 리볼버(성우:아마미야 소라,일러스트:Spirtie)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ ■\n□ ● □\n■ □ ■\n버프칸의 모든총기에게 사속 20%, 회피 20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**진압신호**\n지속시간 동안 아군 전원 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/14.png")    
            await client.send_message(channel,embed=embed) 
        elif "글록 17" in message.content or "글록" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "아스트라 리볼버(성우:토쿠이 소라,일러스트:Rain Lan)",
            ) 
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ ■\n□ ● ■\n■ □ ■\n버프칸의 모든총기에게 명중 64%, 회피 30%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**기선제압**\n지속시간 동안 적 전체 화력 감소",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/15.png")    
            await client.send_message(channel,embed=embed)

        elif "톰슨" in message.content or "님톰총" in message.content or "시카고 타자기" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "톰슨(성우:타네다 리사,일러스트:NS)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n□ ● □\n■ □ □\n버프칸의 돌격소총에게 화력 12%, 회피 15%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**포스쉴드**\n자신의 피해를 막는 왜곡방벽을 9999점 생성한다",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/16.png")    
            await client.send_message(channel,embed=embed) 

        elif "m3" in message.content or "M3" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M3(성우:야마네 노조미,일러스트:November)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n■ ● □\n□ □ □\n버프칸의 돌격소총에게 명중 40%, 회피 30%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**수류탄**\n폭발한 위치의 2.5반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/17.png")    
            await client.send_message(channel,embed=embed)

        elif "MAC-10" in message.content or "mac-10" in message.content or "잉그램"in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M3(성우:오구라 유이,일러스트:오구라 유이r)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:00",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● □\n■ □ □\n버프칸의 돌격소총에게 화력 12%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**연막탄**\n폭발 위치의 2.5 반경에 적의 사속/이속을 감소시키는 연막이 발생.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/18.png")    
            await client.send_message(channel,embed=embed)

        elif "FMG-9" in message.content or "fmg-9" in message.content or "2지역한정"in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "FMG-9(성우:세리자와 유우,일러스트:NorthAbyssor)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n□ ● □\n■ □ □\n버프칸의 돌격소총에게 명중 40%, 회피 30%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**회피기동**\n지속시간 동안 자신의 회피 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/19.png") 
            await client.send_message(channel,embed=embed)

        elif "vector" in message.content or "VECTOR" in message.content or"벡터" in message.content:
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "Vector(성우:하야미 사오리,일러스트:SA)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:35",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n■ ● □\n□ □ □\n버프칸의 돌격소총에게 사속 25%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**소이탄**\n소이탄을 던져 1.5 반경에 피해를 주고 매 0.33초마다 화상 대미지를 입히는 지역을 생성",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/20.png")    
            await client.send_message(channel,embed=embed)

        elif "ppsh-41" in message.content or "PPSH-41" in message.content or"퍄퍄사" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "PPSh-41(성우:우에사카 스미레,일러스트:和茶)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:50",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ ■ □\n버프칸의 돌격소총에게 화력 10%, 사속 5%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**수류탄**\n폭발한 위치의 2.5반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/21.png")    
            await client.send_message(channel,embed=embed)


        elif "pps-43" in message.content or "PPS-43" in message.content or"핑파샤" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "PPS-43(성우:우에사카 스미레,일러스트:两卡车)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:10",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● □\n■ □ □\n버프칸의 돌격소총에게 화력 12%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**수류탄**\n폭발한 위치의 2.5반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/22.png")    
            await client.send_message(channel,embed=embed)

        elif "pp-90" in message.content or "PP-90" in message.content or"란코" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "PP-90(성우:아오이 시키,일러스트:NIXOO)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:20",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n□ ● □\n■ □ □\n버프칸의 돌격소총에게 화력 12%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**회피기동T**\n지속시간 동안 자신의 회피 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/23.png")    
            await client.send_message(channel,embed=embed)

        elif "pp-2000" in message.content or "PP-2000" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "PP-2000(성우:히나타 타마리,일러스트:NoriZC)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:10",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n□ ● □\n■ □ □\n버프칸의 돌격소총에게 화력 10%, 명중 25% ",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**수류탄**\n폭발한 위치의 2.5반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/24.png")    
            await client.send_message(channel,embed=embed)

        elif "mp40" in message.content or " MP40" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "MP40(성우:마츠이 에리코,일러스트:废人)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n□ ● □\n■ □ □\n버프칸의 돌격소총에게 명중 25%, 회피20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**소이탄**\n소이탄을 던져 1.5 반경에 피해를 주고 매 0.33초마다 화상 데미지를 입히는 구간을 생성",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/25.png")    
            await client.send_message(channel,embed=embed)

        elif "mp5" in message.content or " MP5" in message.content or "우유" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "MP5(성우:무카이야마 나오미,일러스트:Saru)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:20",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n□ ● □\n■ □ □\n버프칸의 돌격소총에게 명중 40%, 치명률 20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**포스쉴드**\n자신의 피해를 막는 왜곡방벽을 9999점 생성한다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/26.png")    
            await client.send_message(channel,embed=embed)

        elif "스콜피온" in message.content or "사소리" in message.content or "전갈" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "스콜피온(성우:마츠이 에리코,일러스트:SA)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:00",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n■ ● □\n□ □ □\n버프칸의 돌격소총에게 사속 15%, 명중 50%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**소이탄**\n소이탄을 던져 1.5 반경에 피해를 주고 매 0.33초마다 화상 데미지를 입히는 구간을 생성",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/27.png")    
            await client.send_message(channel,embed=embed)

        elif "mp7" in message.content or " MP7" in message.content or "엠피칠" in message.content or "엠삐칠" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "MP7(성우:Lynn,일러스트:戏言咸咸)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:18(중형제조 한정)",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● □\n■ □ □\n버프칸의 돌격소총에게 사속 15%, 명중 25%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**현월무희**\n지속시간 동안 자신의 사속, 명중이 감소하지만 기동력, 회피 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/28.png")    
            await client.send_message(channel,embed=embed)

        elif "스텐" in message.content or "스텐 mk.ll" in message.content or "스텡" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "스텐 Mk.ll(성우:마츠이 에리코,일러스트:SA)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● □\n■ □ □\n버프칸의 돌격소총에게 명중 10%, 회피 30%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**수류탄**\n폭발한 위치의 2.5반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/29.png")    
            await client.send_message(channel,embed=embed)

        elif "베레타 38형" in message.content or "베레타" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "베레타 38형(성우:타카하시 하루카,일러스트:ALLENES)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n□ ● □\n■ □ □\n버프칸의 돌격소총에게 화력 5%, 사속 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**섬광탄**\n폭발한 위치의 2.5반경 내의 적에게 기절을 건다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/31.png")    
            await client.send_message(channel,embed=embed)

        elif "마이크로 우지" in message.content or "우지" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "마이크로 우지(성우:오오니시 사오리,일러스트:死盖)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ ■ □\n버프칸의 돌격소총에게 화력 18%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**소이탄**\n폭소이탄을 던져 1.5 반경에 피해를 주고 매 0.33초마다 화상 데미지를 입히는 구간을 생성",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/32.png")    
            await client.send_message(channel,embed=embed)

        elif "m45" in message.content or "M45" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M45(성우:타카하시 미카코,일러스트:TAMAXI)",
            ) 
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:20",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n□ ● □\n■ □ □\n버프칸의 돌격소총에게 사속 10%, 회피 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**연막탄**\n폭발 위치의 2.5 반경에 적의 사속/이속을 감소시키는 연막이 발생",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/33.png")    
            await client.send_message(channel,embed=embed)

        elif "m1 개런드" in message.content or "M1 개런드" in message.content or "개런드" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M1 개런드(성우:타네다 리사,일러스트:哈路卡)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "04:00",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ □\n버프칸의 권총에게 스킬 쿨타임 12% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**정밀저격**\n1.5초간 조준한 후에 공격하던 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/34.png")    
            await client.send_message(channel,embed=embed)

        elif "m1a1" in message.content or "M1A1" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M1A1(성우:미모리 스즈코,일러스트:哈路卡)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ ■ □\n버프칸의 권총에게 스킬 쿨타임 12% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**고속사격T**\n지속시간 동안 자신의 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/35.png")    
            await client.send_message(channel,embed=embed)

        elif "m1a1" in message.content or "M1A1" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M1A1(성우:미모리 스즈코,일러스트:哈路卡)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ ■ □\n버프칸의 권총에게 스킬 쿨타임 12% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**고속사격T**\n지속시간 동안 자신의 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/35.png")    
            await client.send_message(channel,embed=embed)

        elif "스프링필드" in message.content or "춘전이" in message.content or "춘전" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "스프링필드(성우:호리에 유이,일러스트:多元菌)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "04:25",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ □\n버프칸의 권총에게 스킬 쿨타임 15% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**저격개시**\n1.5초간 조준한 후에 가장 멀리있는 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/36.png")    
            await client.send_message(channel,embed=embed)

        elif "m14" in message.content or "M14" in message.content or "씹새" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M14(성우:호리에 유이,일러스트:多元菌)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ ■\n버프칸의 권총에게 스킬 쿨타임 12% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/37.png")    
            await client.send_message(channel,embed=embed)

        elif "m21" in message.content or "M21" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M21(성우:키타무라 에리,일러스트:卑しい人间)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ ■ □\n버프칸의 권총에게 스킬 쿨타임 12% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**목표제거**\n1.5초간 조준한 후에 특정 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/38.png")    
            await client.send_message(channel,embed=embed)

        elif "모신나강" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "모신나강(성우:키타무라 에리,일러스트:卑しい人间)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "04:10",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● □\n□ ■ □\n버프칸의 권총에게 스킬 쿨타임 15% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**저격개시**\n1.5초간 조준한 후에 가장 멀리있는 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/39.png")    
            await client.send_message(channel,embed=embed)

        elif "SVT-38" in message.content or "svt-38" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "이테 카오리(성우:키타무라 에리,일러스트:Sola7764)"
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ □\n버프칸의 권총에게 스킬 쿨타임 10% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**목표제거**\n1.5초간 조준한 후에 특정 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/40.png")    
            await client.send_message(channel,embed=embed)

        elif "시모노프" in message.content or "sks"in message.content or "SKS" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "이테 카오리(성우:스자키 아야,일러스트:Phantania)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ ■ □\n버프칸의 권총에게 스킬 쿨타임 10% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**고속사격**\n지속시간 동안 자신의 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/41.png")    
            await client.send_message(channel,embed=embed)

        elif "PTRD" in message.content or "ptrd" in message.content or "남반구" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "PTRD(성우:시미즈 아이,일러스트:Evan揚)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "04:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ □ □\n버프칸의 권총에게 스킬 쿨타임 15% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**확인사살**\n2초간 조준한 후에 최전방의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/42.png")    
            await client.send_message(channel,embed=embed)  

        elif "SVD" in message.content or "svd" in message.content or "스브드" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "SVD(성우:타나카 미나미,일러스트:幻象黒兎)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "04:15",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ ■\n버프칸의 권총에게 스킬 쿨타임 15% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**고속사격**\n지속시간 동안 자신의 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/43.png")    
            await client.send_message(channel,embed=embed)  

        elif "SV-98" in message.content or "sv-98" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "SV-98(성우:하나다 마미코,일러스트:幻象黑兔)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● □\n□ □ ■\n버프칸의 권총에게 스킬 쿨타임 12% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**확인사살**\n1.5초간 조준한 후에 최전방의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/44.png")    
            await client.send_message(channel,embed=embed)  

        elif "Kar98k" in message.content or "카구팔" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "Kar98k(성우:카야노 아이,일러스트:芙芙酱)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "04:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ ■\n버프칸의 권총에게 스킬 쿨타임 18% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**이중저격**\n1초씩 두번 조준 사격하며 각각 현재 타깃에게 대미지를 입힌다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/46.png")    
            await client.send_message(channel,embed=embed)  

        elif "G43" in message.content or "g43" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "G43(성우:야마네 노조미,일러스트:河马)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:10",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ ■\n버프칸의 권총에게 스킬 쿨타임 10% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**고속사격N**\n지속시간 동안 자신의 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/47.png")    
            await client.send_message(channel,embed=embed)   

        elif "wa2000" in message.content or "WA2000" in message.content or "와쟝" in message.content or "와쨩"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "WA2000(성우:토마츠 하루카,일러스트:多元菌)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "04:50",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ □\n버프칸의 권총에게 스킬 쿨타임 18% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**고속사격**\n지속시간 동안 자신의 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/47.png")    
            await client.send_message(channel,embed=embed)

        elif "56식 반" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "56식 반(성우:카리야 루이,일러스트:KAN)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ ■ □\n버프칸의 권총에게 스킬 쿨타임 12% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/49.png")    
            await client.send_message(channel,embed=embed)  

        elif "리엔필드" in message.content or "리엔"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "리엔필드(성우:토마츠 하루카,일러스트:Rei)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "05:00",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ ■ □\n버프칸의 권총에게 스킬 쿨타임 18% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/50.png")    
            await client.send_message(channel,embed=embed)

        elif "FN-49" in message.content or "fn-49"in message.content or"요요요"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "FN-49(성우:미사키 마미,일러스트:Bison仓鼠)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:10 ",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ ■\n버프칸의 권총에게 스킬 쿨타임 10% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/51.png")    
            await client.send_message(channel,embed=embed)

        elif "BM59" in message.content or "bm59"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "BM59(성우:츄조 토모요,일러스트:原子Dan)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:20 ",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ □\n버프칸의 권총에게 스킬 쿨타임 10% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**고속사격**\n지속시간 동안 자신의 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/52.png")    
            await client.send_message(channel,embed=embed)

        elif "NTW-20" in message.content or "ntw-20"in message.content or "노태우"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "NTW-20(성우:카야노 아이,일러스트:RAN)",
            ) 
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "04:45 ",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ □\n버프칸의 권총에게 스킬 쿨타임 18% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**확인사살**\n2초간 조준한 후에 최전방의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/53.png")    
            await client.send_message(channel,embed=embed)

        elif "M16A1" in message.content or "m16a1"in message.content or "우리형" in message.content or "m16" in message.content or "M16" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M16A1(성우:야마네 노조미,일러스트:海猫络合物)",
            ) 
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ ■\n□ ● □\n□ ■ ■\n버프칸의 기관단총에게 화력 10%, 회피12%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**섬광탄**\n폭발한 위치의 2.5반경 내의 적에게 기절을 건다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/54.png")    
            await client.send_message(channel,embed=embed)

        elif "M4A1" in message.content or "m4a1"in message.content or "시나몬" in message.content or "시나몬롤" in message.content or "엠포" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M4A1(성우:토마츠 하루카,일러스트:海猫络合物)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ ■\n□ ● ■\n□ ■ ■\n버프칸의 돌격소총에게 화력 18%, 치명률30%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개T**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/55.png")    
            await client.send_message(channel,embed=embed)

        elif "M4 SOPMOD2" in message.content or "m4 sopmod2"in message.content or "솦모" in message.content or "소프모드" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M4 SOPMOD2(성우:타무라 유카리,일러스트:海猫络合物)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● ■\n□ □ ■\n버프칸의 기관단총에게 명중 50%, 회피12%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**살상류탄**\n폭발한 위치의 1.5반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/56.png")    
            await client.send_message(channel,embed=embed)

        elif "ST AR-15" in message.content or "st ar-15"in message.content or "스타" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "ST AR-15(성우:카토 에미리,일러스트:LIN+)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● ■\n□ □ ■\n버프칸의 기관단총에게 사속 10%, 회피12%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**고속사격T**\n지속시간 동안 자신의 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/57.png")    
            await client.send_message(channel,embed=embed)

        elif "AK-47" in message.content or "ak-47"in message.content or "ak47" in message.content or "AK47"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "AK-47(성우:사토 리나,일러스트:厕所董事长)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:20",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● □\n□ ■ □\n버프칸의 기관단총에게 회피 18%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**기습공격**\n지속시간 동안 자신의 화력, 명중 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/58.png")    
            await client.send_message(channel,embed=embed)

        elif "AK-74U" in message.content or "ak-74u"in message.content or "질싸유" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "AK-74U(성우:타카하시 하루카,일러스트:音符(Infukun))",
            )
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● □\n■ □ □\n버프칸의 돌격소총에게 화력 15%, 명중 25%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**거부반응**\n지속시간 동안 자신이 공격한 적은 일정 시간 동안 화력, 명중 감소 (엘리트 적은 효과 반감)",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/59.png")    
            await client.send_message(channel,embed=embed)

        elif "AS VAL" in message.content or "as val"in message.content or "아스발" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "AS VAL(성우:우에사카 스미레,일러스트:防弹乳牛)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ □ □\n버프칸의 기관단총에게 화력 25%, 사속 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개N**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/60.png")    
            await client.send_message(channel,embed=embed)

        elif "stg44" in message.content or "STG44"in message.content or "StG44" in  message.content or "서태지" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "StG44(성우:카야노 아이,일러스트:八才)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:00",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ □\n버프칸의 기관단총에게 회피 20%, 명중 60%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**파열류탄**\n유탄을 발사하여 폭발한 위치의 1/2.5/4 반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/61.png")    
            await client.send_message(channel,embed=embed)

        elif "G41" in message.content or "g41"in message.content or "댕댕이" in  message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "G41(성우:쿠기미야 리에,일러스트:NS)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "04:05",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ ■\n버프칸의 기관단총에게 회피 15%, 명중 50%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개T**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/62.png")    
            await client.send_message(channel,embed=embed)

        elif "G36C" in message.content or "지상렬씨" in  message.content or "상렬씨" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "G36C(성우:후지타 아카네,일러스트:Parsley)",
            )
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● □\n■ □ □\n버프칸의 돌격소총에게화력 10%, 사속 8%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**포스실드**\n자신의 피해를 막는 왜곡방벽을 9999점 생성한다",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/104.png")    
            await client.send_message(channel,embed=embed)

        elif "G3" in message.content or "g3" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "G3(성우:요시오카 카오리,일러스트:PHI)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:50",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ □ □\n버프칸의 기관단총에게 사속 20%, 명중 50%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**살상류탄**\n폭발한 위치의 1.5반경 내의적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/63.png")    
            await client.send_message(channel,embed=embed)

        elif "G36" in message.content or "g36" in message.content or "지상렬"in message.content or "상렬"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "G36(성우:코시미즈 아미,일러스트:薯子Imoko)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ ■\n버프칸의 기관단총에게 화력 30%, 사속 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개T**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/64.png")    
            await client.send_message(channel,embed=embed)

        elif "HK416" in message.content or "hk416" in message.content or "흥국이"in message.content or "흥국"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "HK416(성우:노나카 아이,일러스트:NIXOO)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:55",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ ■\n버프칸의 기관단총에게 화력 40%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**살상류탄**\n폭발한 위치의 1.5반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/65.png")    
            await client.send_message(channel,embed=embed)

        elif "56-1식" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "56-1식(성우:아마미야 소라,일러스트:CanceR)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:25",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ ■\n버프칸의 기관단총에게 회피 15%, 치명률 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**파열류탄**\n폭발한 위치의 1/2.5/4반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/66.png")    
            await client.send_message(channel,embed=embed)

        elif "L85A1" in message.content or "l85a1"in message.content or "하지메 마시떼"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "L85A1(성우:아야미야 유키코,일러스트:MKiiiiii)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:50",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ □\n□ ● □\n□ □ □\n버프칸의 기관단총에게 화력 20%, 명중 50%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**강행돌파**\n지속시간 동안 자신의 화력, 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/68.png")    
            await client.send_message(channel,embed=embed)

        elif "FAMAS" in message.content or "famas"in message.content or "파마스"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "FAMAS(성우:아야미야 유키코,일러스트:MKiiiiii)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● □\n□ □ ■\n버프칸의 기관단총에게 화력 20%, 명중 50%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**파열류탄**\n폭발한 위치의 1/2.5/4반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/69.png")    
            await client.send_message(channel,embed=embed)

        elif "FNC" in message.content or "fnc"in message.content or "초코" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "FNC(성우:야츠루기 스미레,일러스트:麻将)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:20",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ □\n버프칸의 기관단총에게 명중 50%, 회피 12%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개**\n지속시간 동안 자신의 화력 증가.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/70.png")    
            await client.send_message(channel,embed=embed)

        elif "갈릴" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "갈릴(성우:미타라이 카린,일러스트:lyo)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ □\n버프칸의 기관단총에게 명중 50%, 회피 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**호흡조절**\n지속시간 동안 자신의 명중 증가.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/71.png")    
            await client.send_message(channel,embed=embed)

        elif "TAR-21" in message.content or "tar-21" in message.content or "타보르" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "TAR-21(성우:마이하라 유메,일러스트:木Shiyo)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ ■\n버프칸의 기관단총에게 회피 18%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**강행돌파**\n지속시간 동안 자신의 화력, 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/72.png")    
            await client.send_message(channel,embed=embed)

        elif "AUG" in message.content or "aug" in message.content or "어그" in message.content or "아우게" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "AUG(성우:와키 아즈미,일러스트:芙芙酱)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ ■\n□ ● ■\n□ ■ ■\n버프칸의 모든총기에게 화력 12%, 명중 20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**장례식의 비**\n지속시간 동안 자신의 명중이 감소하지만 사속이 150이 되고 난사한다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/73.png")    
            await client.send_message(channel,embed=embed)

        elif "sig-510" in message.content or "SIG-510" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "SIG-510(성우:아마노 미라이,일러스트:Spirtie)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ ■\n버프칸의 모든총기에게 화력 20%, 사속 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/74.png")    
            await client.send_message(channel,embed=embed)

        elif "M1918" in message.content or "m1918" in message.content or "바쟝" in message.content or "바쨩" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M1918(성우:유우키 아오이,일러스트:水乌龟)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "06:25",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n● □ ■\n□ □ □\n버프칸의 산탄총에게 화력 15%, 장갑 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개MG**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/75.png")    
            await client.send_message(channel,embed=embed)

        elif "M2HB" in message.content or "m2hb" in message.content or "초로이" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M2HB(성우:이와마츠 이즈미,일러스트:15K)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "06:10",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n● □ ■\n□ □ □\n버프칸의 산탄총에게 화력 22%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**사중극점**\n3회 일반 공격 후 4회째 공격을 강화",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/77.png")    
            await client.send_message(channel,embed=embed)

        elif "M60" in message.content or "m60" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M60(성우:이토 아스카,일러스트:Mika Pikazo)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "06:10",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "● □ ■\n□ □ □\n□ □ ■\n버프칸의 산탄총에게 화력 10%, 사속 8%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개N-MG**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/78.png")    
            await client.send_message(channel,embed=embed)

        elif "M249 SAW" in message.content or "M249" in message.content or "m249 saw" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M249 SAW(성우:난죠 요시노,일러스트:雪樱樱)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n● □ ■\n□ □ ■\n버프칸의 산탄총에게 사속 12%, 명중 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**준비만전N**\n야간작전에서 지속시간 동안 자신의 화력 증가, 발사중인 탄띠에 탄 추가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/79.png")    
            await client.send_message(channel,embed=embed)

        elif "M1919A4" in message.content or "M1919"in message.content or "m1919a4" in message.content or "m1919" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M1919A4(성우:요시다 사치요,일러스트:As109)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "05:40",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ □ □\n● □ □\n버프칸의 산탄총에게 명중 25%, 장갑 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**사냥충동**\n지속시간 동안 자신의 명중 상승,모든 공격이 치명타가 된다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/80.png")    
            await client.send_message(channel,embed=embed)

        elif "LWMMG" in message.content or "lwmmg"in message.content or "람쥐" in message.content or "람지" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "LWMMG(성우:닛타 히요리,일러스트:RFF)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "05:10",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n● □ ■\n□ □ □\n버프칸의 산탄총에게 화력 10%, 사속 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**사냥충동**\n지속시간 동안 자신의 명중 상승,모든 공격이 치명타가 된다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/81.png")    
            await client.send_message(channel,embed=embed)

        elif "DP28" in message.content or "dp28" in message.content or "군주님" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "DP28(성우:이카다이 카나에,일러스트:BIBIA)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "05:00",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ □ □\n● □ ■\n버프칸의 산탄총에게 사속 15%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**준비만전**\n지속시간 동안 자신의 화력 증가 발사중인 탄띠에 탄 추가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/82.png")    
            await client.send_message(channel,embed=embed)

        elif "RPD" in message.content or "rpd" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "RPD(성우:노미즈 이오리,일러스트:Sam_Ashton)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n● □ □\n□ □ ■\n버프칸의 산탄총에게 사속 16%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개MG**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/84.png")    
            await client.send_message(channel,embed=embed)

        elif "PK" in message.content or "pk" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "PK(성우:나즈카 카오리,일러스트:木Shiyo)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "06:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n● □ ■\n□ □ □\n버프칸의 산탄총에게 화력 18%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**사중극점**\n3회 일반 공격 후 4회째 공격을 강화",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/85.png")    
            await client.send_message(channel,embed=embed)

        elif "mg42" in message.content or "MG42" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "MG42(성우:요코야 사야카,일러스트:Spirtie)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "05:50",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "● □ □\n□ □ □\n□ □ ■\n버프칸의 산탄총에게 화력 22%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개MG**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/86.png")    
            await client.send_message(channel,embed=embed)

        elif "mg34" in message.content or "MG34" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "MG34(성우:츄조 토모요,일러스트:Spirtie)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "05:00",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ □ □\n● □ □\n버프칸의 산탄총에게 화력 20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개MG**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/87.png")    
            await client.send_message(channel,embed=embed)

        elif "mg3" in message.content or "MG3" in message.content or "망3" in message.content or "망삼"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "MG3(성우:타네다 리사,일러스트:猫头神)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "06:30",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n● □ □\n□ □ ■\n버프칸의 산탄총에게 화력 10%, 명중 15%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**준비만전**\n지속시간 동안 자신의 화력 증가 발사중인 탄띠에 탄 추가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/88.png")    
            await client.send_message(channel,embed=embed)

        elif "브렌" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "브렌(성우:아마미야 소라,일러스트:废人)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "05:20",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "● □ ■\n□ □ □\n□ □ ■\n버프칸의 산탄총에게 사속 10%, 명중 12%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**준비만전**\n지속시간 동안 자신의 화력 증가 발사중인 탄띠에 탄 추가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/89.png")    
            await client.send_message(channel,embed=embed)

        elif "FNP-9" in message.content or "fnp-9"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "FNP-9(성우:코가 아오이,일러스트:Bison仓鼠)",
            )
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:25",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ ■ □\n● ■ □\n■ ■ □\n버프칸의 모든총기에게 사속 20%, 명중 40%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**퇴로차단**\n지속시간 동안 적 전체 회피 감소",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/90.png")    
            await client.send_message(channel,embed=embed)

        elif "MP-446" in message.content or "mp-446"in message.content or "바이킹"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "MP-446(성우:코가 아오이,일러스트:Bison仓鼠)",
            )
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:25",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ ■ □\n■ ● □\n■ ■ □\n버프칸의 모든총기에게 화력 28%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**격발차단**\n지속시간 동안 적 전체 사속 감소",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/91.png")    
            await client.send_message(channel,embed=embed)

        elif "spector m4" in message.content or "SPECTOR M4"in message.content or "스펙터"in message.content or "Spector M4" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "Spector M4(성우:우에마 에미,일러스트:MKiiiiii)",
            )
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:20",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n■ ● □\n□ □ □\n버프칸의 돌격소총에게 화력 28%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**회피기동**\n지속시간 동안 자신의 회피 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/92.png")    
            await client.send_message(channel,embed=embed)

        elif "IDW" in message.content or "idw"in message.content or "아디따"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "IDW(성우:이토 아스카,일러스트:Ki桑)",
            )
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:10",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● □\n■ □ □\n버프칸의 돌격소총에게 화력 28%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**회피기동**\n지속시간 동안 자신의 회피 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/93.png")    
            await client.send_message(channel,embed=embed)

        elif "64식" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "64식(성우:이토 아스카,일러스트:Ki桑)",
            )
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:25",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n■ ● □\n□ □ □\n버프칸의 돌격소총에게 사속 20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**섬광탄**\n폭발한 위치의 2.5반경 내의 적에게 기절을 건다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/94.png")    
            await client.send_message(channel,embed=embed)

        elif "한양조 88식" in message.content or "한양조" in  message.content or "한조"in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "한양조 88식(성우:아이사카 유카,일러스트:团子)",
            )
            embed.add_field (
                name = "종류",
                value = "RF",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:25",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ □\n버프칸의 권총에게 스킬 쿨타임 12% 감소",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개N**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/95.png")    
            await client.send_message(channel,embed=embed)

        elif "그리즐리 MkV" in message.content or "그리즐리" in  message.content or "곰" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "그리즐리 MkV(성우:이타타니 아야카,일러스트:REALMBW)",
            )
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:10",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ ■ □\n□ ● ■\n■ ■ □\n버프칸의 모든총기에게 화력 30%, 회피 20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**일제사격**\n지속시간 동안 아군 전원 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/96.png")    
            await client.send_message(channel,embed=embed)

        elif "M950A" in message.content or "m950a" in  message.content or "캘리코" in message.content or "미역" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "M950A(성우:코가 아오이,일러스트:音符)",
            )
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "01:05",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ ■\n□ ● □\n■ □ ■\n버프칸의 모든총기에게 사속 30%, 명중 50%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**진압신호**\n지속시간 동안 아군 전원 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/97.png")    
            await client.send_message(channel,embed=embed)

        elif "SPP-1" in message.content or "spp-1" in  message.content or "물로리" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "SPP-1(성우:오오츠보 유카,일러스트:麻将)",
            )
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ ■ □\n□ ● □\n■ ■ □\n버프칸의 모든총기에게 화력 12%, 명중 90%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**퇴로차단**\n지속시간 동안 적 전체 회피 감소",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/98.png")    
            await client.send_message(channel,embed=embed)

        elif "MK23" in message.content or "mk23" in  message.content or "참피" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "Mk23(성우:아카오 히카루,일러스트:雪樱樱)",
            )
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:50",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● ■\n■ □ □\n버프칸의 모든총기에게 화력 36%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**일제사격N**\n지속시간 동안 아군 전원 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/99.png")    
            await client.send_message(channel,embed=embed)

        elif "P7" in message.content or "p7" in  message.content or "삐칠" in message.content or "피칠" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "P7(성우:쿠로사와 토모요,일러스트:Saru)",
            )
            embed.add_field (
                name = "종류",
                value = "HG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "00:55",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ ■ ■\n□ ● □\n■ ■ ■\n버프칸의 모든총기에게 사속 20%, 회피 24%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**엄호개시**\n지속시간 동안 아군 전체 회피 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/100.png")    
            await client.send_message(channel,embed=embed)

        elif "UMP9" in message.content or "ump9" in  message.content or "움뀨" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "UMP9(성우:노토 마미코,일러스트:ZAGALA)",
            )
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:15",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● □\n■ □ □\n버프칸의 모든총기에게 사속 12%, 명중 30%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**섬광탄**\n폭발한 위치의 2.5반경 내의 적에게 기절을 건다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/101.png")    
            await client.send_message(channel,embed=embed)

        elif "UMP40" in message.content or "ump40" in  message.content or "움사공" in message.content or "사공" in message.content :           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "UMP40(성우:우에마 에미,일러스트:Renatus-Z)",
            )
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ ■ ■\n□ ● □\n□ ■ ■\n버프칸의 기관단총에게 치명률 500%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "*과중부하**\n2초마다 자신에게 이하의 효과를주는 스택을 쌓는다. 최대 5스택.발동 전 : 회피 상승 / 화력 감소 발동 후 : 회피 감소 / 화력 상승",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/102.png")    
            await client.send_message(channel,embed=embed)

        elif "UMP45" in message.content or "ump45" in  message.content or "움사오" in message.content or "사오" in message.content :           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "UMP45(성우:미네우치 토모미,일러스트:ZAGALA)",
            )
            embed.add_field (
                name = "종류",
                value = "SMG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "4성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "■ □ □\n■ ● □\n■ □ □\n버프칸의 돌격소총에게 화력 18%, 치명률 30%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**연막탄**\n폭발 위치의 2.5 반경에 적의 사속/이속을 감소시키는 연막이 발생",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/103.png")    
            await client.send_message(channel,embed=embed)

        elif "OTS-12" in message.content or "ots-12" in  message.content or "티스" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "OTS-12(성우:우치야마 유미,일러스트:林檎爱す)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:10",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● ■\n□ □ □\n버프칸의 기관단총에게 화력 18%, 치명률 30%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**고속사격T**\n지속시간 동안 자신의 사속 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/105.png")    
            await client.send_message(channel,embed=embed)

        elif "FAL" in message.content or "fal" in  message.content or "괄" in message.content or "120엔" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "FAL(성우:요시무라 하루카,일러스트:水乌龟)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "03:45",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● ■\n□ □ ■\n버프칸의 기관단총에게 회피 20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**유탄폭격**\n3발의 유탄을 연속으로 발사하여 각 발당 반경 1.5범위 내의 적들에게 피해를 입힌다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/106.png")    
            await client.send_message(channel,embed=embed)
        elif "F2000" in message.content or "f2000" in  message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "F2000(성우:토쿠이 소라,일러스트:hanasa)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "02:45",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ □\n□ ● ■\n□ □ □\n버프칸의 기관단총에게 화력 20%, 회피 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/107.png")    
            await client.send_message(channel,embed=embed)

        elif "CZ-805" in message.content or "cz-805" in  message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "CZ-805(성우:우치다 마아야,일러스트:木子翔)",
            )
            embed.add_field (
                name = "종류",
                value = "AR",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "3성",
                inline = False
            )
            embed.add_field (
                name = "제조시간",
                value = "제조 불가",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n□ ● □\n□ □ ■\n버프칸의 기관단총에게 사속 25%, 명중 50%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**파열류탄**\n유탄을 발사하여 폭발한 위치의 1/2.5/4 반경 내의 적에게 피해를 준다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/108.png")    
            await client.send_message(channel,embed=embed)

        elif "MG5" in message.content or "mg5" in  message.content or "망고" in message.content or "망가오" in message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "CZ-805(성우:코시미즈 아미,일러스트:音符)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "5성",
                inline = False
            )
            embed.add_field (
                 name = "제조시간",
                value = "06:45",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n● □ □\n□ □ ■\n버프칸의 산탄총에게 화력 10%, 장갑 10%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**사중극점**\n3회 일반 공격 후 4회째 공격을 강화",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/109.png")    
            await client.send_message(channel,embed=embed)

        elif "FG42" in message.content or "fg42" in  message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "FG42(성우:이토 아스카,일러스트:叽困)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                 name = "제조시간",
                value = "04:50",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "□ □ ■\n● □ □\n□ □ ■\n버프칸의 산탄총에게 명중 30%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**사냥충동**\n지속시간 동안 자신의 명중 상승, 모든 공격이 치명타가 된다.",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/110.png")    
            await client.send_message(channel,embed=embed)

        elif "AAT-52" in message.content or "aat-52" in  message.content:           
            embed = discord.Embed(color = 0x1e90ff) 
            embed.add_field (
                name = "이름",
                value = "AAT-52(성우:우치야마 유미,일러스트:Lino)",
            )
            embed.add_field (
                name = "종류",
                value = "MG",
                inline = True
            )
            embed.add_field (
                name = "희귀도",
                value = "2성",
                inline = False
            )
            embed.add_field (
                 name = "제조시간",
                value = "04:50",
                inline = True
            )
            embed.add_field (
                name = "진형버프",
                value = "● □ □\n□ □ □\n□ □ ■\n버프칸의 산탄총에게 사속 20%",
                inline = False
            )
            embed.add_field (
                name = "스킬",
                value = "**화력전개N-MG**\n지속시간 동안 자신의 화력 증가",
                inline = True
            )
            embed.set_image(url = "http://img.iorph.com/gf/111.png")    
            await client.send_message(channel,embed=embed)

        



client.run(token)   
