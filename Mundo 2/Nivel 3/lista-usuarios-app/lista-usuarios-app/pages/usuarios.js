import Link from 'next/link'
import styles from '../styles/Usuarios.module.css'
const usuarios = [
    {
        nome: "André Eppinghaus",
        id: 1
    },
    {
        nome: "Luiz Estevão",
        id: 2
    },
    {
        nome: "Vicente Calfo",
        id: 3
    }
]
export default function Usuarios() {
    return (
        < >
            <h1>Lista Usuários</h1>
            {
            usuarios.map(usuario=> (
                <Link legacyBehavior href={`/usuario/${usuario.id}`}>
                    <a className={styles.card}>
                        <h2>{usuario.nome}</h2>
                    </a>
                </Link>
                ))
            }
        </>
    )
}