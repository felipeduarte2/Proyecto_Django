from django import template

register = template.Library()

@register.filter(name='traducir_fecha')
def traducir_fecha(fecha):
    # traducir al español el mes
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 
             'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    mes = meses[fecha.month - 1]
    
    f = """
    <div class="notification">
        <div class="notiglow"></div>
        <div class="notiborderglow"></div>
        <div class="notititle">Traducción</div>
        <div class="notibody">"""+ f"{fecha.day} de {mes} del {fecha.year}" +"""</div>
    </div>
    <style>
      .notification {
        display: flex;
        flex-direction: column;
        isolation: isolate;
        position: relative;
        width: 18rem;
        height: 6rem;
        background: #29292c;
        border-radius: 1rem;
        overflow: hidden;
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        font-size: 16px;
        --gradient: linear-gradient(to bottom, #2eadff, #3d83ff, #7e61ff);
        --color: #32a6ff
      }

      .notification:before {
        position: absolute;
        content: "";
        inset: 0.0625rem;
        border-radius: 0.9375rem;
        background: #18181b;
        z-index: 2
      }

      .notification:after {
        position: absolute;
        content: "";
        width: 0.25rem;
        inset: 0.65rem auto 0.65rem 0.5rem;
        border-radius: 0.125rem;
        background: var(--gradient);
        transition: transform 300ms ease;
        z-index: 4;
      }

      .notification:hover:after {
        transform: translateX(0.15rem)
      }

      .notititle {
        color: var(--color);
        padding: 0.65rem 0.25rem 0.4rem 1.25rem;
        font-weight: 500;
        font-size: 1.1rem;
        transition: transform 300ms ease;
        z-index: 5;
      }

      .notification:hover .notititle {
        transform: translateX(0.15rem)
      }

      .notibody {
        color: #99999d;
        padding: 0 1.25rem;
        transition: transform 300ms ease;
        z-index: 5;
      }

      .notification:hover .notibody {
        transform: translateX(0.25rem)
      }

      .notiglow,
      .notiborderglow {
        position: absolute;
        width: 20rem;
        height: 20rem;
        transform: translate(-50%, -50%);
        background: radial-gradient(circle closest-side at center, white, transparent);
        opacity: 0;
        transition: opacity 300ms ease;
      }

      .notiglow {
        z-index: 3;
      }

      .notiborderglow {
        z-index: 1;
      }

      .notification:hover .notiglow {
        opacity: 0.1
      }

      .notification:hover .notiborderglow {
        opacity: 0.1
      }

      .note {
        color: var(--color);
        position: fixed;
        top: 80%;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
        font-size: 0.9rem;
        width: 75%;
      }
    </style>
    """
    return f




