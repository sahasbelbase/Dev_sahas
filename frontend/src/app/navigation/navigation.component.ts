import { Component, ViewChild } from '@angular/core';
import { MatDrawer } from '@angular/material/sidenav';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent {
  @ViewChild('leftDrawer') leftDrawer!: MatDrawer;
  @ViewChild('bottomDrawer') bottomDrawer!: MatDrawer;

  constructor() {}

  navigationList = [
    { name: 'hotel', link: '/hotel', icon: 'hotel' },
    { name: 'customer', link: '/customer', icon: 'people' },
    { name: 'branch', link: '/branch', icon: 'house' },
    { name: 'invoice', link: '/invoice', icon: 'receipt' },
    { name: 'room', link: '/room', icon: 'meeting_room' } // Assuming 'meeting_room' is the MatIcon for room
  ];

  toggleLeftDrawer() {
    this.leftDrawer.toggle();
  }

  toggleBottomDrawer() {
    this.bottomDrawer.toggle();
  }
}
