import Link from "next/link"
import buscaNoticias from '../lib/noticias'

const Home = () => ({ noticias }) => {
  return (
    <>
      <h1>Notícias</h1>
      <ul>
      {noticias.map(({ slug, title }) => (
          <li key={slug}>
              <Link href={'/${slug}'}>
              <a>{title}</a>
              </Link>
          </li>
      ))}
      </ul>
    </>
  );
};

export async function getStaticProps() {
    return {
        props: {
            noticias: await buscaNoticias(),
        },
    };
}
export default Home;