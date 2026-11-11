# Educational infographic v3: legend-row redesign (no stacked right-aligned labels possible).
from PIL import Image, ImageDraw, ImageFont
import random, math

W,H = 1600,900
BG=(249,250,251); INK=(17,24,39); SUB=(75,85,99); MUTED=(156,163,175)
BLUE=(0,75,232); YELLOW=(251,191,36); GREEN=(5,150,105); PURPLE=(124,58,237); RED=(220,38,38)
F=lambda n,s: ImageFont.truetype(f'/tmp/fonts/SourceSans3-{n}.ttf',s)

img=Image.new('RGB',(W,H),BG)
d=ImageDraw.Draw(img)
random.seed(7)

def stipple_planet(cx,cy,r,density=1.0,exclude=None):
    n=int(r*r*0.30*density)
    for _ in range(n):
        a=random.uniform(0,2*math.pi); rr=r*math.sqrt(random.random())
        x,y=cx+rr*math.cos(a), cy+rr*math.sin(a)
        if exclude:
            skip=False
            for ex0,ey0,ex1,ey1 in exclude:
                if ex0-8<=x<=ex1+8 and ey0-8<=y<=ey1+8:
                    skip=True; break
            if skip: continue
        s=((x-cx)+(y-cy)*0.3)/r
        p=0.15+0.85*max(0,(s+1)/2)
        if random.random()<p*0.5:
            sz=random.choice([1,1,2])
            d.ellipse([x-sz,y-sz,x+sz,y+sz],fill=BLUE)

stipple_planet(1536,84,44,density=0.85)
stipple_planet(1552,866,96,density=0.9,exclude=[(0,0,1340,H),(0,H-96,1380,H)])

for ang in range(0,360):
    a=math.radians(ang)
    x=-40+150*math.cos(a); y=H+30+64*math.sin(a)
    if random.random()<0.45:
        sz=random.choice([2,3])
        d.ellipse([x-sz,y-sz,x+sz,y+sz],fill=YELLOW)

# headline
d.text((90,58),"Where your fee goes.",font=F('Light',62),fill=INK)
d.text((90,132),"Burned, then re-minted.",font=F('Light',62),fill=BLUE)

# three step cards
y0=286; cardw=428; gap=38
cards=[
 ("1 · YOU PAY A FEE", ["An app burns POKT to pay", "for one relay."]),
 ("2 · 97.5% COMES BACK", ["Since PIP-41 (Feb 2026)", "97.5 of every 100 returns."]),
 ("3 · IT SPLITS FOUR WAYS", ["Governance sets the shares.", "The last 2.5% never returns."]),
]
x=90
for ci,(title,lines) in enumerate(cards):
    d.rounded_rectangle([x,y0,x+cardw,y0+132],18,fill=(255,255,255),outline=(233,236,240),width=2)
    d.text((x+26,y0+20),title,font=F('Semibold',25),fill=BLUE)
    for i,ln in enumerate(lines):
        d.text((x+26,y0+62+i*32),ln,font=F('Regular',25),fill=SUB)
    if ci < len(cards)-1:
        d.line([x+cardw+10,y0+66,x+cardw+gap-12,y0+66],fill=MUTED,width=3)
        d.polygon([(x+cardw+gap-12,y0+59),(x+cardw+gap-2,y0+66),(x+cardw+gap-12,y0+73)],fill=MUTED)
    x+=cardw+gap

# hero split bar
sy=534; sx=90; sw=1420; sh=92
d.text((90,488),"THE SPLIT OF EVERY SETTLEMENT",font=F('Semibold',23),fill=INK)
shares=[(0.79,BLUE,"79%","Suppliers","serve the relays"),
        (0.14,GREEN,"14%","Validators","produce blocks"),
        (0.045,PURPLE,"4.5%","DAO","ecosystem funding"),
        (0.025,YELLOW,"2.5%","Service owners","maintain services")]
x=sx
for frac,col,pct,*_ in shares:
    w=int(sw*frac)
    d.rectangle([x,sy,x+w-3,sy+sh],fill=col)
    if frac>0.10:
        d.text((x+22,sy+20),pct,font=F('Bold',42),fill=(255,255,255))
    x+=w

# legend row: four equal cells (chip + name + pct + role) — cannot overlap by construction
ly=sy+sh+38
cell=(1510-90)//4
for i,(frac,col,pct,name,role) in enumerate(shares):
    cx0=90+i*cell
    d.rounded_rectangle([cx0,ly+2,cx0+24,ly+26],6,fill=col)
    d.text((cx0+36,ly),f"{name}  {pct}",font=F('Semibold',26),fill=INK)
    d.text((cx0+36,ly+32),role,font=F('Regular',21),fill=MUTED)

# deflation note
dy=ly+86
d.rounded_rectangle([90,dy,1510,dy+58],14,fill=(254,242,242),outline=(254,226,226),width=2)
d.ellipse([118,dy+21,134,dy+37],fill=RED)
d.text((150,dy+14),"The remaining 2.5% of the original burn is never re-minted: every relay makes POKT slightly deflationary.",font=F('Regular',26),fill=RED)

# footer
fy=H-84
lx,lyf,lr=100,fy+28,26
d.ellipse([lx-lr,lyf-lr,lx+lr,lyf+lr],fill=BLUE)
d.ellipse([lx-0.64*lr,lyf-0.64*lr,lx+0.64*lr,lyf+0.64*lr],outline=(255,255,255),width=6)
d.text((lx+40,lyf-22),"pocket",font=F('Semibold',30),fill=INK)
d.text((lx+185,lyf-14),"Sources: docs.pocket.network — token/faq + node-operators/rewards-economics · live values Nov 12 2026",
       font=F('Regular',19),fill=MUTED)

img.save('/home/ubuntu/pocket-research/where-your-fee-goes.png')
# orbit arc around corner planet (kept in safe corner)
for ang in range(0,360):
    a=math.radians(ang)
    x=1552+118*math.cos(a); y=866+46*math.sin(a)
    if x>1400 and y>780 and random.random()<0.3:
        d.ellipse([x-1,y-1,x+1,y+1],fill=(96,124,242))
print('saved v5')
