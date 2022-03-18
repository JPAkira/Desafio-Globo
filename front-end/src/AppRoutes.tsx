import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom"

import { Cadastro } from './pages/Cadastro'
import { Relatorios } from './pages/cards'

export function AppRoutes() {
    return (
        <Router>
            <Routes>
                <Route path="/cadastro" element={<Cadastro />} />
                <Route path="/" element={<Relatorios />} />
            </Routes>
        </Router>
    )
}