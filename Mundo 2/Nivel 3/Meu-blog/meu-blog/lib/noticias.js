import { promises as fs } from "fs";
import path from "path";
import matter from "gray-matter";

const buscaNoticias = async () => {
  const diretorioNoticias = path.join(process.cwd( ), "noticias");
  const filenames = await fs.readdir (diretorioNoticias);

  return await Promise.all(
    filenames.map(async (filename) => {
        const filePath = path. join(diretorioNoticias, filename);
        const fileContents = await fs.readFile(filePath, "utf8")
        const document = matter(fileContents);

        return {
            slug: filename.replace(/\.md$/, ""), // Usado na URL da notícia
            title: document.data.title,
            date: document.data.date,
            markdown: document.content,
        }
    })
  );
};
export default buscaNoticias;