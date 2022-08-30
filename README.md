### ETF (School of Electrical Engineering) - Master Academic Studies - * Computational Genomics (13M111GI) *

#### 💥 Objectives

Implementation of a Probability Diffusion Algorithm from [CTD: An information-theoretic algorithm to interpret sets of metabolomic
and transcriptomic perturbations in the context of graphical models](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008550) (Table 2.)

<details>
  <summary>💥 Requirements (Serbian)</summary>
Smatrati da je matrica susednosti data na ulazu kao Padas dataframe koji se učitava iz csv fajla i da je u pitanju matrica susednosti neusmerenog težinskog grafa.
- Algoritam implementirati rekurzivno (kao što je opisano u radu) i iterativno i porediti performanse u pogledu vremena izvršavanja i memorijskog zauzeća.
- Trenutno se u algoritmu za difuziju ½ verovatnoće rasipa na susede, a ½ ostaje u čvoru (linije 8, 9, 10 i 11 pseudokoda u navedenom radu). Proširiti algoritam tako da implementirana funkcija prima parametar alfa koji određuje koji se procenat verovatnoće prenosi na susede, npr. ako je alfa = 0.7, prenosi se 70% verovatnoće, a 30% ostaje u čvoru. 
- Definisati set testova koji će meriti performanse i porediti identičnost rezultata rekurzivne i iterativne implementacije na raznovrsnom skupu grafova. Testovi treba da pokriju četiri kategorije grafova u pogledu broja čvorova: male (5-15 čvorova), srednje (15-100) čvorova, veće (100 - 1000) i velike (preko 1000 čvorova), svaku kategoriju sa bar 5 testova koji se suštinski razlikuju u topologiji grafa. U testovima se pokreće implementirana funkcija za difuziju verovatnoće, počevši od slučajno izabranog čvora grafa, sa početnom verovatnoćom 0.5.
- Kreirati vizuelizaciju za testove iz kategorije malih grafova u kojim će čvorovi grafa biti gradaciono obojeni po količini verovatnoće u njima na kraju difuzije.
</details>

💥 Check out a [video presentation of the solution](https://www.youtube.com/watch?v=ZRm_73ZqpJQ&ab_channel=Mili%C4%8Devi%C4%87Nikola). (also in Serbian)

💥 Test it out!
- If you want to run our solution you can do it in a following way:
  - this
  - this 
  - this 


