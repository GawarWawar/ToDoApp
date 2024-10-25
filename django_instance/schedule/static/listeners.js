document.addEventListener('alpine:init', () => {
    Alpine.data('expireDateChecker', (el) => ({
        expiredStatus: false,
        expireDate: '',
        visible: false,
        bgcolor_on_mouseover: '',
        standard_color:'',
        completedStatus: '',

        // Main start process
        startSetUp(){
            // Get expiration date from the HTML attribute 'data-expiration-date'
            this.expireDate = el.getAttribute('data-expire-date');
            // Get completion status from the HTML attribute 'data-completed'
            this.completedStatus = el.getAttribute('data-completed').toLowerCase() === "true";
            
            // Check expiration immediately on load
            this.checkExpiration();
        },

        // Start the periodic check for Tasks
        startTaskCheck() {
            this.startSetUp()
            this.setStandrdColor();

            // Style background based on setStandrdColor
            el.style.backgroundColor = this.standard_color

            // Set up a periodic check every 10 seconds
            setInterval(() => {
                this.checkExpiration();
                this.setStandrdColor();
            }, 10000); // 10000ms = 10 seconds

        },

        // Start the periodic check for Projects
        startProjectCheck(){
            this.startSetUp()

            // Set up a periodic check every 10 seconds
            setInterval(() => {
                this.checkExpiration();
            }, 10000); // 10000ms = 10 seconds
        },

        // Check if the current date is past the expiration date
        checkExpiration() {
            const expireDate = new Date(this.expireDate);
            const currentDate = new Date();

            // Update 'expiredStatus' state based on completedStatus and date comparison
            if (this.completedStatus){
                this.expiredStatus = false;
            } else {
                this.expiredStatus = currentDate > expireDate;
            }
        },

        // Set bgcolor based on completedStatus and expiredStatus
        setStandrdColor() {
            if (this.completedStatus) {
                // If task was completed set green color
                this.standard_color = "#81C784";                
            } else if (this.expiredStatus) {
                // If task expired set red color
                this.standard_color = '#ee6b6e';
            } else {
                this.standard_color = '';
            }
        }

    }));
});
