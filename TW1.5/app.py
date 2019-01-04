from flask import Flask, render_template
import random


app = Flask(__name__)

links = ([
    "https://preview.redd.it/83r3r9298a821.jpg?width=960&crop=smart&auto=webp&s=d07c7f5c42634ad16d31bd4fb9506ccab67a3225",
    "https://i.redd.it/8wc7g0c1e8821.jpg",
    "https://preview.redd.it/skj1eo2698821.jpg?width=960&crop=smart&auto=webp&s=fefa4766b443529aa657864b46ff0f9291792636",
    "https://i.redd.it/sidl7fszu9821.jpg",
    "https://preview.redd.it/m2tpvxysx7821.jpg?width=640&crop=smart&auto=webp&s=8bf15c4685f9ad01a484f4af627090426fc74e15",
    "https://preview.redd.it/7jf698clk8821.jpg?width=960&crop=smart&auto=webp&s=fb64f98eeca76c04c4dda31ec6b970795e092ab7",
    "https://i.redd.it/66kno7jxva821.jpg",
    "https://preview.redd.it/h0r9ofz6dc821.jpg?width=640&crop=smart&auto=webp&s=e98b4784d58991e9697695e4508a0b497afcb75c",
    "https://preview.redd.it/phoh7eqd88821.jpg?width=640&crop=smart&auto=webp&s=d1d703797654aafbb8d8b4e63df5c14f91c32af9",
    'https://i.imgflip.com/2qcigf.jpg',
    'https://i.imgflip.com/2qci9q.jpg',
    'https://i.imgflip.com/2qciw2.jpg',
    'https://i.imgflip.com/2qcj27.jpg',
    'https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/48982014_2188360371182891_6839815859322486784_n.jpg?_nc_cat=1&_nc_ht=scontent-vie1-1.xx&oh=0e5f57ed7ae990a2246399c58e1a8d49&oe=5C8DA05D',
    'https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/48944674_2188359994516262_7164055816809480192_n.jpg?_nc_cat=1&_nc_ht=scontent-vie1-1.xx&oh=dfcfba350480e0e3b897a112759f4a23&oe=5CCEC475',
    'https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/49101899_2188359871182941_794369392694525952_n.jpg?_nc_cat=1&_nc_ht=scontent-vie1-1.xx&oh=60def46acdcdc06bdec290ce94b06742&oe=5C917196',
    'https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/49024008_2188359361182992_3277243927282843648_o.jpg?_nc_cat=106&_nc_ht=scontent-vie1-1.xx&oh=61470f8530b74ae078a29c0c0eb3adbd&oe=5CCD1CD0',
    'https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/49012495_2188358601183068_3562409238678470656_o.jpg?_nc_cat=111&_nc_ht=scontent-vie1-1.xx&oh=b013592b772b4e70a91812340dac8c49&oe=5C93B3EC',
    'https://i.redd.it/ytw5pl5wia821.jpg',
    "https://preview.redd.it/9sznppd2lc821.jpg?width=960&crop=smart&auto=webp&s=5a80293c31e3f62bd5bf01affb6a7810f71ea781",
    "https://i.redd.it/kd1zbynxyc821.jpg",
    "https://preview.redd.it/a3lr8thl9a821.jpg?width=960&crop=smart&auto=webp&s=bcc0e5c00b246e74c73faccc09c8ccb7dfd37d6d",
    "https://preview.redd.it/h26gurr2wa821.jpg?width=960&crop=smart&auto=webp&s=e5a23dca699fc3a2d1c649c22a8ec95feb7f0d9d",
    "https://preview.redd.it/xqizx0hazb821.jpg?width=640&crop=smart&auto=webp&s=77dd72696ddea00aa9a122d132e49a884bc1c24e",
    "https://i.redd.it/s26daot40d821.png",
    "https://i.redd.it/hm1ksiksmc821.jpg",
    "https://i.redd.it/gh20vqdh5b821.jpg",
    "https://preview.redd.it/tdkopr5947821.jpg?width=960&crop=smart&auto=webp&s=7ddee92fe271b8a1e46bd28f323631b9a25347e1",
    "https://i.redd.it/f1tudvqhr8821.jpg",
    "https://preview.redd.it/t18ygpopad821.jpg?width=960&crop=smart&auto=webp&s=114b1e5cec447b3866e44ef00d47b442b5026b08",
    "https://i.redd.it/y8v1no31l5821.jpg"
])


@app.route('/')
def home_page():
    link = random.choice(links)
    return render_template("index.html", link=link)


if __name__ == '__main__':
    app.run()
