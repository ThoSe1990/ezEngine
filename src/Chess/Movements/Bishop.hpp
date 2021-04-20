#ifndef _CHESS_MOVEMENTS_BISHOP_HPP_
#define _CHESS_MOVEMENTS_BISHOP_HPP_

#include "Chess/Movements/Movement.hpp" 

class Bishop : public Movement
{
public:
    Bishop(const std::shared_ptr<ChesspieceComponent>& Chesspiece) : Movement(Chesspiece) { }

    void CreateValidMovements() override
    {
        createValidationMultiSteps(Movements::right, Movements::up);
        createValidationMultiSteps(Movements::right, Movements::down);
        createValidationMultiSteps(Movements::left, Movements::down);
        createValidationMultiSteps(Movements::left, Movements::up);
    }
};

#endif