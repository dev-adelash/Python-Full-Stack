import {Engine} from './engine';const fixture=globalThis as typeof globalThis & {commerceFixture?:Engine};export const engine=fixture.commerceFixture??=new Engine();
