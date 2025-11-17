// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Require Assert
 * @dev Program 028
 */
contract Program028 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Require Assert");
    }
}
