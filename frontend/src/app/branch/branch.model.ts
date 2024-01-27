export interface Branch {
    hotelId: number;
    name: string;
    branchId: number;
    branchAddress?: {
      country: string;
      city: string;
      streetName: string;
    };
  }