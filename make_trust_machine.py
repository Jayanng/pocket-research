# Educational Pocket Graphic v1: "How Pocket pays without trusting anyone"
# Topic: Session -> Claim -> Proof -> Settlement lifecycle (the trust-minimization core mechanic).
# Different topic from the fee-split graphic (that one = money flows; this one = the verification machine).
# Brand language: off-white #F9FAFB, Pocket blue #004BE8, stipple planets, yellow torus, Source Sans 3.
from PIL import Image, ImageDraw, ImageFont
import random, math

W,H = 1600,900
BG=(249,250,251); INK=(17,24,39); SUB=(75,85,99); MUTED=(156,163,175)
BLUE=(0,75,232); YELLOW=(251,191,36); GREEN=(5,150,105); RED=(220,38,38); SOFT=(233,242,255)
F=lambda n,s: ImageFont.truetype(f'/tmp/fonts/SourceSans3-{n}.ttf',s)

img=Image.new('RGB',(W,H),BG)
d=ImageDraw.Draw(img)
random.seed(11)

def stipple_planet(cx,cy,r,density=1.0,exclude=None,color=BLUE):
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
            d.ellipse([x-sz,y-sz,x+sz,y+sz],fill=color)

stipple_planet(1536,86,44,density=0.85)
stipple_planet(1552,866,96,density=0.9,exclude=[(0,0,1340,H),(0,H-96,1380,H)])
for ang in range(0,360):
    a=math.radians(ang)
    x=-40+150*math.cos(a); y=H+30+64*math.sin(a)
    if random.random()<0.45:
        sz=random.choice([2,3])
        d.ellipse([x-sz,y-sz,x+sz,y+sz],fill=YELLOW)

# headline
d.text((90,54),"How Pocket pays without",font=F('Light',60),fill=INK)
d.text((90,128),"trusting anyone.",font=F('Light',60),fill=BLUE)
d.text((90,208),"Four steps, checked by math, not by faith.",font=F('Regular',27),fill=SUB)

# timeline spine
sy=668
d.line([120,sy+36,1460,sy+36],fill=(209,213,219),width=3)

# four stage cards
stages=[
 ("1 · SESSION","60 blocks","The network deterministically assigns suppliers to your app. No scheduler, no favorites: every node computes the same answer.",BLUE),
 ("2 · CLAIM","+11 blocks, open 10","After serving, each supplier reports what it did. On-chain, public, and locked in before any checking.",GREEN),
 ("3 · PROOF","opens +1 after claims, open 10","The chain picks ONE relay at random. The supplier must produce cryptographic evidence for exactly that one.",YELLOW),
 ("4 · SETTLEMENT","automatic","Pass the check, get paid. Fail, and cheating collapses: a liar gets caught ~50% per session.",RED),
]
cardw=322; gap=32; x=90
for i,(title,tim,desc,col) in enumerate(stages):
    y0=290; ch=330
    d.rounded_rectangle([x,y0,x+cardw,y0+ch],18,fill=(255,255,255),outline=(233,236,240),width=2)
    # number chip
    d.rounded_rectangle([x+24,y0+22,x+cardw-24,y0+62],10,fill=SOFT)
    d.text((x+38,y0+30),title,font=F('Semibold',22),fill=BLUE)
    # timeline marker on spine
    cx=x+cardw//2
    d.ellipse([cx-9,sy+27,cx+9,sy+45],fill=col)
    d.line([cx,y0+ch,cx,sy+46],fill=(209,213,219),width=2)
    # duration pill
    d.text((x+24,y0+76),tim,font=F('Semibold',21),fill=col)
    # description, wrapped
    words=desc.split(); lines=[]; cur=''
    for w in words:
        test=(cur+' '+w).strip()
        if d.textlength(test,font=F('Regular',21.5))>cardw-48:
            lines.append(cur); cur=w
        else: cur=test
    lines.append(cur)
    yy=y0+116
    for ln in lines[:8]:
        d.text((x+24,yy),ln,font=F('Regular',21.5),fill=SUB); yy+=30
    if i<3:
        d.line([x+cardw+6,y0+66,x+cardw+gap-10,y0+66],fill=MUTED,width=3)
        d.polygon([(x+cardw+gap-12,y0+59),(x+cardw+gap-2,y0+66),(x+cardw+gap-12,y0+73)],fill=MUTED)
    x+=cardw+gap

# the insight band (tax-audit analogy from docs)
by=716
d.rounded_rectangle([90,by,1510,by+96],14,fill=SOFT,outline=(214,229,252),width=2)
d.ellipse([118,by+40,136,by+58],fill=BLUE)
d.text((150,by+14),"Why cheating fails: like a tax audit. The supplier commits its claim BEFORE",font=F('Regular',25),fill=(30,58,138))
d.text((150,by+52),"knowing which relay will be audited. Falsify half your relays and you're caught ~50% of the time, every session.",font=F('Regular',25),fill=(30,58,138))

# footer
fy=H-84
# official Pocket logo lockup (docs.pocket.network/logo-black.svg), rendered at 52px height
from PIL import Image as _Img
_pocket_logo=_Img.open('/tmp/pocket-logo-footer.png').convert('RGBA')
img.paste(_pocket_logo,(96,fy-4),_pocket_logo)


fy=H-84
# official Pocket logo lockup (docs.pocket.network/logo-black.svg), rendered at 52px height
from PIL import Image as _Img
_pocket_logo=_Img.open('/tmp/pocket-logo-footer.png').convert('RGBA')
img.paste(_pocket_logo,(96,fy-4),_pocket_logo)

d.text((340,fy+8),"Source: docs.pocket.network, Protocol > Sessions, Claims & Proofs · verified Nov 13 2026",
       font=F('Regular',19),fill=MUTED)

img.save('/home/ubuntu/pocket-research/trust-machine.png')
print('saved', img.size)
