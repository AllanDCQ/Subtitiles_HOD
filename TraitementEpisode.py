from pathlib import Path

import logging

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(level=logging.INFO,
                    filename=BASE_DIR / 'user.log',
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')


class TraitementEpisode:
    def get_episodes(episode_debut: int, episode_fin: int, chemin_episodes: list) -> object:
        """

        Args:
            nombre_episode: Le nombre d'épisodes
            chemin_episodes: Une liste pour stocker les chemins des épisodes

        Returns:
            object: Retourne la liste des chemins des épisodes

        """
        try:
            for i in range(episode_debut, episode_fin + 1, 1):
                logging.info("En attente de récupération des sous-titres de l'épisode " + str(i) + " ...")
                try:
                    chemin_episodes.append(BASE_DIR / f"episodes/episode_{i}.txt")
                    logging.info(chemin_episodes[i - 1])
                    logging.info("Récupération effectuée avec succès.")

                except:
                    logging.critical("Echec de la récupération.")
                    pass
            logging.info("Succès récupération des sous titres.")

        except:
            logging.critical("Echec récupération des sous titres.")

        return chemin_episodes

    def lecture_episodes(nombre_episode: int, chemin_episodes: list, contenu_episode: list) -> object:
        """

        Args:
            nombre_episode: Le nombre d'épisodes
            chemin_episodes: La liste des chemins des épisodes
            contenu_episode: La liste de sortie des sous-titres

        Returns:
            object: Retourne la liste des sous-titres des épisodes

        """
        logging.info("En attente de lecture des sous-titres des " + str(nombre_episode) + " épisodes")
        try:
            for j in range(0, nombre_episode, 1):
                contenu_episode.append(chemin_episodes[j].read_text())
            logging.info("Succès lecture des sous titres.")
        except:
            logging.critical("Echec lecture des sous titres.")

        return contenu_episode

    def traitement(nombre_episode: int, contenu_episode: list, list_mots: list) -> object:
        """

        Args:
            nombre_episode: Le nombre d'épisodes
            contenu_episode: La liste des sous-titres
            list_mots: La liste de sortie contenant tous les mots

        Returns:
            object: Retourne une liste de tous les mots des sous titres

        """
        logging.info("En attente de traitement des sous-titres des " + str(nombre_episode) + " épisodes")

        try:
            for j in range(0, nombre_episode, 1):
                contenu_episode[j] = contenu_episode[j].replace("<i>", "")
                contenu_episode[j] = contenu_episode[j].replace("</i>", "")
                contenu_episode[j] = contenu_episode[j].replace("\n", " ")
                contenu_episode[j] = contenu_episode[j].replace(".", " ")
                contenu_episode[j] = contenu_episode[j].split(" ")

                for i in range(0, len(contenu_episode[j])):

                    if contenu_episode[j][i].isalpha() and len(contenu_episode[j][i]) > 4:
                        list_mots.append(contenu_episode[j][i].lower())

                logging.info("Succès traitement de l'épisode " + str(j + 1))

            logging.info("Succès traitement des sous titres.")

        except:
            logging.critical("Echec traitement des sous titres.")

        return list_mots
