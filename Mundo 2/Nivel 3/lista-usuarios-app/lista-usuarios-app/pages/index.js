import Link from 'next/link'
import styles from '../styles/Home.module.css'
export default function Home() {
    return (
        < >
        <Link legacyBehavior href="/usuarios">
            <a className={styles.button}>Lista de Usuários</a>
        </Link>
        </>
    )
}