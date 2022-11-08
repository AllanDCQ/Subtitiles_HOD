import collections
import pprint as pp
from typing import Any, Optional
import typer
from TraitementEpisode import TraitementEpisode as TE

app = typer.Typer()


@app.command('run')
def main(nb: Optional[int] = typer.Argument(0, help="Quel est la taille de la liste à afficher ?"),
         episode_d: Optional[int] = typer.Argument(0, help="Premier épisode dans lequel chercher (min : 1)"),
         episode_f: Optional[int] = typer.Argument(0, help="Dernier épisode dans lequel chercher (max : 7)")) :
    """
    Liste des mots les plus utilisés dans la série 'House Of The Dragon en fonctions des options
    """

    if nb == 0 :
        nb = typer.prompt("Quel est la taille de la liste à afficher ?")

    if episode_d == 0:
        episode_d = typer.prompt("Premier épisode dans lequel chercher (min : 1)")

    if episode_f == 0:
        episode_f = typer.prompt("Dernier épisode dans lequel chercher (max : 7)")

    Liste_mots(int(episode_d), int(episode_f), int(nb))


@app.command('all')
def all():
    """
    Liste tous les mots les plus utilisés dans la série 'House Of The Dragon
    """
    Liste_mots(1, 7, 10)


def Liste_mots(episode_debut:int,episode_fin: int, nombre_classement: int):
    """
    Args:
        nombre_episode: Le nombre d'épisodes
        nombre_classement: La taille du classement
    """
    contenu_episode: list[Any] = []
    chemin_episodes: list[Any] = []
    list_mots: list[Any] = []

    TE.get_episodes(episode_debut,episode_fin, chemin_episodes)
    TE.lecture_episodes(episode_fin, chemin_episodes, contenu_episode)
    TE.traitement(episode_fin, contenu_episode, list_mots)
    counter = collections.Counter(list_mots)

    print("Les mots les plus utilisés dans la série 'House Of The Dragon' sont :")
    pp.pprint(counter.most_common(nombre_classement))


if __name__ == "__main__" :
    app()
