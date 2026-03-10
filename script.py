
html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Vasco da Gama - Contador de Seca</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@300;400;700&display=swap');

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      background: #000;
      color: #fff;
      font-family: 'Roboto', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      overflow: hidden;
      padding: 20px;
      position: relative;
    }

    /* Fundo com imagem do escudo enviada pelo usuário */
    .bg-escudo {
      position: fixed;
      inset: 0;
      background-image: 
        url('EscudoDoVascoDaGama.svg.jpg'),
        radial-gradient(circle at 50% 30%, rgba(255,255,255,0.06) 0%, transparent 60%),
        linear-gradient(180deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.9) 50%, #000 100%);
      background-size: 60% auto, cover, cover;
      background-position: center 20%, center, center;
      background-repeat: no-repeat;
      z-index: -2;
      opacity: 0.85;
    }

    /* Máscara de transparência gradual de cima para baixo */
    .bg-escudo::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, 
        transparent 0%, 
        transparent 20%,
        rgba(0,0,0,0.4) 40%,
        rgba(0,0,0,0.7) 60%,
        rgba(0,0,0,1) 100%);
      pointer-events: none;
    }

    .clube {
      font-family: 'Bebas Neue', cursive;
      font-size: clamp(2rem, 6vw, 4rem);
      letter-spacing: 8px;
      color: #fff;
      text-shadow: 0 4px 8px rgba(0,0,0,0.8);
      margin-bottom: 6px;
      z-index: 10;
    }

    .subtitulo {
      font-size: clamp(0.9rem, 2.5vw, 1.2rem);
      font-weight: 300;
      color: #ccc;
      letter-spacing: 3px;
      text-transform: uppercase;
      margin-bottom: 30px;
      z-index: 10;
    }

    .ultimo-titulo {
      background: linear-gradient(135deg, #111 0%, #333 50%, #111 100%);
      border: 1px solid #666;
      border-radius: 12px;
      padding: 14px 32px;
      margin-bottom: 40px;
      box-shadow: 
        0 0 20px rgba(0,0,0,0.8),
        inset 0 1px 0 rgba(255,255,255,0.1);
      z-index: 10;
    }

    .ultimo-titulo p {
      font-size: clamp(0.8rem, 2vw, 1rem);
      color: #fff;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 4px;
    }

    .ultimo-titulo h2 {
      font-family: 'Bebas Neue', cursive;
      font-size: clamp(1.5rem, 4vw, 2.2rem);
      color: #fff;
      letter-spacing: 4px;
      text-shadow: 0 2px 8px rgba(0,0,0,0.8);
    }

    .seca-label {
      font-size: clamp(0.85rem, 2vw, 1rem);
      letter-spacing: 4px;
      color: #aaa;
      text-transform: uppercase;
      margin-bottom: 10px;
      z-index: 10;
    }

    /* Dias: apenas branco puro, sem brilho/glow */
    .dias {
      font-family: 'Bebas Neue', cursive;
      font-size: clamp(6rem, 22vw, 16rem);
      line-height: 0.9;
      color: #fff;
      text-shadow: 0 4px 12px rgba(0,0,0,0.9); /* Apenas sombra preta para legibilidade */
      letter-spacing: -4px;
      margin-bottom: 6px;
      z-index: 10;
    }

    .dias-label {
      font-family: 'Bebas Neue', cursive;
      font-size: clamp(1.2rem, 4vw, 2rem);
      letter-spacing: 10px;
      color: #ddd;
      margin-bottom: 40px;
      z-index: 10;
    }

    .unidades {
      display: flex;
      gap: clamp(16px, 4vw, 48px);
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 30px;
      z-index: 10;
    }

    .unidade {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .unidade span.valor {
      font-family: 'Bebas Neue', cursive;
      font-size: clamp(1.8rem, 6vw, 3.5rem);
      color: #fff;
      text-shadow: 0 2px 8px rgba(0,0,0,0.8);
      line-height: 1;
      min-width: 3ch;
    }

    .unidade span.label {
      font-size: clamp(0.6rem, 1.5vw, 0.8rem);
      letter-spacing: 3px;
      color: #888;
      text-transform: uppercase;
      margin-top: 4px;
    }

    .separador {
      font-family: 'Bebas Neue', cursive;
      font-size: clamp(1.8rem, 6vw, 3.5rem);
      color: #666;
      align-self: flex-start;
      padding-top: 2px;
    }

    .rodape {
      font-size: 0.7rem;
      color: #666;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-top: 10px;
      z-index: 10;
    }

    .linha {
      width: 60px;
      height: 2px;
      background: linear-gradient(90deg, transparent, #fff, transparent);
      margin: 0 auto 30px;
      opacity: 0.6;
    }
  </style>
</head>
<body>

  <div class="bg-escudo"></div>

  <div class="clube">Club de Regatas Vasco da Gama</div>
  <div class="subtitulo">Rio de Janeiro · Fundado em 1898</div>

  <div class="ultimo-titulo">
    <p>🏆 Último Título</p>
    <h2>Campeão do Carioca 2016</h2>
  </div>

  <div class="linha"></div>

  <div class="seca-label">Dias sem título</div>
  <div class="dias" id="dias">0</div>
  <div class="dias-label">DIAS</div>

  <div class="unidades">
    <div class="unidade">
      <span class="valor" id="horas">0</span>
      <span class="label">Horas</span>
    </div>
    <div class="separador">:</div>
    <div class="unidade">
      <span class="valor" id="minutos">00</span>
      <span class="label">Minutos</span>
    </div>
    <div class="separador">:</div>
    <div class="unidade">
      <span class="valor" id="segundos">00</span>
      <span class="label">Segundos</span>
    </div>
  </div>

  <div class="rodape">Contador atualizado em tempo real · desde 08/05/2016</div>

  <script>
    const tituloDate = new Date('2016-05-08T00:00:00');

    function pad(n) { return String(n).padStart(2, '0'); }

    function atualizar() {
      const agora = new Date();
      const diff = agora - tituloDate;

      const totalSegundos = Math.floor(diff / 1000);
      const totalMinutos  = Math.floor(diff / (1000 * 60));
      const totalHoras    = Math.floor(diff / (1000 * 60 * 60));
      const totalDias     = Math.floor(diff / (1000 * 60 * 60 * 24));

      const minutosRest = totalMinutos % 60;
      const segundosRest = totalSegundos % 60;

      document.getElementById('dias').textContent     = totalDias.toLocaleString('pt-BR');
      document.getElementById('horas').textContent    = totalHoras.toLocaleString('pt-BR');
      document.getElementById('minutos').textContent  = pad(minutosRest);
      document.getElementById('segundos').textContent = pad(segundosRest);
    }

    atualizar();
    setInterval(atualizar, 1000);
  </script>

</body>
</html>'''

with open('vasco_contador_escudo_real.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Site atualizado com escudo real + degradê transparente!")
