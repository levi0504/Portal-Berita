from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    berita = [
        {
            'judul': 'Teknologi AI Mengubah Dunia Pendidikan',
            'tanggal': '11 November 2025',
            'penulis': 'Redaksi Portal Berita',
            'konten': 'Perkembangan kecerdasan buatan (AI) semakin pesat dan mulai diterapkan dalam dunia pendidikan di berbagai negara.'
        },
        {
            'judul': 'Ekonomi Digital Indonesia Terus Tumbuh',
            'tanggal': '10 November 2025',
            'penulis': 'Dewi Lestari',
            'konten': 'Pertumbuhan ekonomi digital Indonesia mencapai 13% pada tahun 2025 berkat perkembangan e-commerce dan startup teknologi.'
        },
        {
            'judul': 'Tips Aman Berinternet di Era Modern',
            'tanggal': '9 November 2025',
            'penulis': 'Ahmad Fauzi',
            'konten': 'Berinternet secara aman sangat penting untuk menjaga privasi dan keamanan data pribadi di dunia maya.'
        }
    ]
    return render_template('index.html', berita=berita)

@app.route('/artikel/<judul>')
def artikel(judul):
    return render_template('artikel.html', judul=judul)

if __name__ == '__main__':
    app.run(debug=True)
