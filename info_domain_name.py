# import whois
import whois 
def is_registered(domain_name):
    """
    Une fonction qui retourne un booléen indiquant 
    si un `domain_name` est enregistré.
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

# # liste de domaines enregistrés et non enregistrés pour tester notre fonction
# domains = [
#     "solutions-web.com",
#     "google.com",
#     "github.com",
#     "unknownrandomdomain.com",
#     "notregistered.co"
# ]
# # itérer sur des domaines
# for domain in domains:
#     print(domain, "est enrégistrer" if is_registered(domain) else "n'est pas enrégistrer")

domain_name = "solutions-web.com"
if is_registered(domain_name):
    whois_info = whois.whois(domain_name)

    # obtenir la date de création
    print("Date de création:", whois_info.creation_date)
    # obtenir la date d'expiration 
    print("Date d'Expiration:", whois_info.expiration_date)

    # # Afficher le serveur WHOIS 
    # print("WHOIS server:", whois_info.whois_server)

    # Afficher tous les infos
    #print(whois_info)