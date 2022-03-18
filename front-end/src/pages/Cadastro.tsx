import { CadastroForm } from "../components/CadastroForm"
import '../assets/Styles/Content.css'
import woman from '../assets/Images/woman.jpg'
import logo from '../assets/Images/brand-insights.svg'
import {NavLink} from 'react-router-dom'

export function Cadastro() {
    return (
        <div className="content">
            <br/>
            <div className="flex-box">
            <img className='logo-imagem' src={logo}></img>
            <img className='menu-avatar-imagem' src={woman}></img>
            <NavLink to='/' >
                <span className="material-icons iconcolor">chevron_left</span>
            </NavLink>
            </div>
            <span className="usuario-content">Olá, Usuário</span>
            <span className="email-content">email@gmail.com</span>
            <br/>
            <span className="titulo-content">Feed de <b>Insights</b></span>
            <br/>
            <CadastroForm />
        </div>
    );
}
