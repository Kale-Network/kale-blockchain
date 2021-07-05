import Unit from './Unit';
import { IS_MAINNET } from './constants';

export default {
  [Unit.KALE]: IS_MAINNET ? 'XCH' : 'TXCH',
};
