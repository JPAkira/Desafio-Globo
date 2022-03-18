import { ChangeList } from "../components/ChangeList"
import '../assets/Styles/Content.css'
import woman from '../assets/Images/woman.jpg'
import logo from '../assets/Images/brand-insights.svg'
import {NavLink} from 'react-router-dom'

export function Relatorios() {
    return (
        <div className="content">
            <br/>
            <div className="flex-box">
            <img className='logo-imagem' src={logo}></img>
            <img className='menu-avatar-imagem' src={woman}></img>
            <NavLink to='/cadastro' >
                <span className="material-icons iconcolor">add</span>
            </NavLink>
            </div>
            <span className="usuario-content">Olá, Usuário</span>
            <span className="email-content">email@gmail.com</span>
            <br/>
            <span className="titulo-content">Feed de <b>Insights</b></span>
            <br/>
            <ChangeList />
        </div>
    );
}
