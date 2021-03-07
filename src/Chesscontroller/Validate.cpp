
#include "Chesscontroller/Validate.hpp"
#include "Chesscontroller/PlayersTurn.hpp"

#include "Movements/MovementsFactory.hpp"

Validate::Validate (std::string PlayerColor, std::string OpponentColor) : playerColor(PlayerColor), opponentColor(OpponentColor)
{

}

void Validate::UpdateGame(Chesscontroller* chesscontroller)
{
    auto [piece, color] = chesscontroller->GetSelectedPieceAndColor();

    auto movements = MovementFactory::Create(piece);
    movements->CreateValidMovements(chesscontroller, piece);

    PlayersTurn* next = new PlayersTurn(chesscontroller, playerColor, opponentColor);
    chesscontroller->SetState(next);
    delete this;
}

