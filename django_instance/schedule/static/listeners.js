document.addEventListener('alpine:init', () => {
    Alpine.data('taskChecker', (el) => ({
        expired: false,
        expireDate: '',
        visible: false,
        bgcolor: '',
        standard_color:'',
        completedStatus: '',

        // Start the periodic check
        startCheck() {
            // Get expiration date from the HTML attribute 'data-expiration-date'
            this.expireDate = el.getAttribute('data-expire-date');
            this.completedStatus = el.getAttribute('data-completed').toLowerCase() === "true";

            // Check expiration immediately on load
            this.checkExpiration();
            this.setStandrdColor();
            el.style.backgroundColor = this.standard_color

            // Set up a periodic check every 10 seconds
            setInterval(() => {
                this.checkExpiration();

            }, 10000); // 10000ms = 10 seconds

        },

        // Check if the current date is past the expiration date
        checkExpiration() {
            const expireDate = new Date(this.expireDate);
            const currentDate = new Date();

            // Update 'expired' state based on date comparison
            if (this.completedStatus){
                this.expired = false;
            } else {
                this.expired = currentDate > expireDate;
            }
            this.setStandrdColor();

        },

        setStandrdColor() {
            if (this.completedStatus) {
                this.standard_color = "#81C784";                
            } else if (this.expired) {
                this.standard_color = '#ee6b6e';
            } else {
                this.standard_color = '';
            }
        }

    }));
});
