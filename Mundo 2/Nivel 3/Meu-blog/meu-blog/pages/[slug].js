import ReactMarkdown from "react-markdown";
import buscaNoticias from "../lib/noticias";

const Noticia = ({ title, date, markdown }) => (
  <article> 
    <h1>{title}</h1>
    <time>{date}</time>
    <ReactMarkdown>{markdown}</ReactMarkdown>
  </article>
);

export const getStaticPaths = async () => {
    const noticias = await buscaNoticias();

    return {
        paths: noticias.map((noticia)=> '/${noticia.slug}'),
        fallback: false,
    };
};

export const getStaticProps = async ({ params: { slug } }) => {
    const noticias = await buscaNoticias();
    const noticia = noticias. find ((noticia) => noticia.slug === slug);
    
    return { props: noticia};
};

export default Noticia;