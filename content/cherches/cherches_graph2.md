---
title: "Graph ta recherche"
date: 2022-03-02
---

Dans le cadre d'un atelier pour le groupe de recherche « Comparative Materialities Research Group » de la *Canadian Comparative Literature Association* (CCLA), la CRCEN a exploré la question du code collaboratif et de la structuration collaborative des données de recherche. 

Cette expérience a amené à créer un code en python (dans le même esprit que [Graph ta thèse](https://blank.blue/cherches/graph-ta-these/)). 

En voici les coulisses : 

## Play (with) me

Le but de l'atelier était de proposer un dispositif pour que les participants codent ensemble un petit script. En parallèle de la recherche d'une interface permettant de coder collaborativement en synchrone, il fallait penser à un *jeu* à proposer aux chercheur.e.s[^1].

[^1]: L'atelier est une préparation de la présentation que la CRCEN fera en juin lors du congrès annuel de CCLA. Le thème de notre groupe est *play*. 

L'an passé nous avons organisé un atelier sur le principe d'écriture collaborative : les participants étaient invités à écrire ensemble dans un pad en ligne[^2].

[^2]: Le pad est disponible [ici](https://stylo.huma-num.fr/article/6139122bb19841001964226a/preview).

Cette année, nous voulions expérimenter un autre type d'écriture toujours en lien avec la question du collaboratif (comme modèle et pratique qui structure une communauté) : le code. 

Mais, 

         il ne s'agissait pas seulement d'expérimenter le code collaboratif synchrone
         il ne s'agissait pas seulement de proposer une introduction à python
         il ne s'agissait pas seulement d'avoir du fun dans l'être ensemble à même un espace d'écriture

Il s'agissait d'appréhender l'espace de programmation comme une forme de structuration d'une pensée qui serait le reflet de notre communauté. 

En ce sens, notre défense demeure inchangée : 

## L'environnement d'écriture est une forme de pensée 

Écho aux Media Studies, ce que nous avions performé l'an passé dans le pad collaboratif (qui est à l'origine d'un article à paraître) devait être renégocié dans un autre environnement d'écriture, selon un langage et une syntaxe différente. 

Il va sans dire que l'atelier nécessitait davantage de préparation : 

- quel dispositif ? 

Il était préférable de trouver un outil en ligne, gratuit, ouvert, qui ne nécessite ni installation ni création de compte pour les participants. 

- quel jeu (& de données) ? 

Soit sous la forme d'exercices ou de tutoriel, nous devions proposer aux participants une *quête* qui réponde à de possibles besoins/intérêts de recherche. En voici, un exemple : 

### Fruit de ta recherche

L'une des idées formulées que je retranscrit ici[^3] était celle de penser un dispositif pour *matcher* les chercheur.e.s selon leurs intérêts de recherche. 

Référence à l'application de rencontre *Fruitz* (qui établit le modèle de la rencontre sur le principe du type de relation recherchée par l'individu), *Fruit de ta recherche* devait proposer aux chercheur.e.s de se « rencontrer » si leurs centres de recherche, selon le type de carrière visée, selon leurs approches, leurs écoles de pensée, etc. 

[^3]: Parce qu'elle serait selon moi à réaliser dans le futur. 

Cette proposition a été écartée pour des questions de délais de réalisation. 

## Les références qui nous lient

Pour l'heure, nous n'avons par trouvé d'environnement approprié pour le code collaboratif synchrone qui corresponde aux besoins de l'atelier. 

Nous avons alors reformulé nos exigences en ces termes : 

Pour les données 

    se recentrer sur un jeu de données disponibles en ligne 
    se concentrer sur des données qui intéressent les chercheur.e.s 
    = les références & Zotero 

Pour le jeu

    proposer aux participants de jouer avec les références d'une librairie Zotero partagée
    préparer un script python en amont pour produire des visualisations de ces données 
    = Jupyter notebook 

Concrètement, nous avons *fetcher* une [bibliothèque Zotero partagée](https://www.zotero.org/groups/4592469/ccla-atelier/library) et produire des visualisations des références avec python afin de réorganiser les structures des données et de montrer les connexions entre les informations éditées. 

Le but de cet atelier n'est pas seulement de jouer avec les données. Nous voulons souligner et démontrer l'importance des références dans nos communautés de recherche et l'importance de structurer ces données. 

Les références ne sont pas seulement des ressources scientifiques, elles font partie de l'identité de nos communautés et le jeu avec ces données est une forme de pensée.

## Graph le retour 

Récupération d'un principe [déjà expérimenté](https://blank.blue/cherches/graph-ta-these/), voilà que je replonge dans python[^4] pour produire un script qui permette de visualiser les liens : 

- [x] entre les références
- [ ] entre les références et les chercheur.e.s
- [ ] entre les chercheur.e.s

Visualisation du Jupyter Notebook : 

<iframe src="/html/CCLA-atelier.html"></iframe>

<a href="/html/CCLA-atelier.html" target="blank">ouvrir dans le navigateur</a>

[^4]: Il faudra prévoir un post pour parler de ma montée en python.



## Networks en image

### Début de l'atelier

<img src="/images/CCLA-Network11.png" alt="" width="1200" height="200"/>

<a href="https://blank.blue/images/CCLA-Network11.png" target="blank">parcourir dans une nouvelle page</a>


### Fin de l'atelier

<img src="/images/CCLA-Network1.png" alt="" width="1200" height="200"/>

<a href="https://blank.blue/images/CCLA-Network1.png" target="blank">parcourir dans une nouvelle page</a>


## Liens utiles 

- [Bibliographie Zotero de l'atelier](https://www.zotero.org/groups/4592469/ccla-atelier/library)
- [Jupyter Notebook de l'atelier](https://gitlab.huma-num.fr/ecrinum/graph-ta-recherche/-/blob/master/CCLA-atelier.ipynb)
- [Repo Gitlab de l'atelier](https://gitlab.huma-num.fr/ecrinum/graph-ta-recherche)