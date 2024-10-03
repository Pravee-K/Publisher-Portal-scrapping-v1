from TabSupport.Tools.Tool import fetch_menu_tabs, driver  # Assuming driver is initialized here
import TabSupport.fees
import TabSupport.admission
import TabSupport.placement
import TabSupport.ranking
import TabSupport.HostelAndInfra
import TabSupport.scholarships
import TabSupport.reviews
import TabSupport.ClgInfo

Fees = TabSupport.fees
Admission = TabSupport.admission
Placement = TabSupport.placement
Ranking = TabSupport.ranking
HostelAndinfra = TabSupport.HostelAndInfra
Scholarships = TabSupport.scholarships
Reviews = TabSupport.reviews
clgINfo = TabSupport.ClgInfo

def main():
    Fees.run()
    # Admission.run()
    # Placement.run()
    # Ranking.run()
    # HostelAndinfra.run()
    # Scholarships.run()
    # Reviews.run()

if __name__ == "__main__":
    main()