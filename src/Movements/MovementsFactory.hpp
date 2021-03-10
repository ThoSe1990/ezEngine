#ifndef _MOVEMENTS_MOVEMENTSFACTORY_HPP_
#define _MOVEMENTS_MOVEMENTSFACTORY_HPP_

#include "Movements/Movements.hpp"
#include "Movements/Pawn.hpp"
#include "Movements/Knight.hpp"
#include "Movements/Bishop.hpp"
#include "Movements/Rook.hpp"
#include "Movements/Queen.hpp"
#include "Movements/King.hpp"


class MovementFactory
{
public:
    static std::unique_ptr<Movement> Create(std::shared_ptr<Chesscontroller>& chesscontroller, Entity* entity)
    {
        Logger::Log(logging::trivial::debug, log_location, "creating movements for " , entity->name);

        ChesspieceComponent* cp = entity->GetComponent<ChesspieceComponent>();
        if (cp->type_.compare("pawn") == 0)
        {
            return std::make_unique<Pawn>(chesscontroller, entity);
        }
        else if (cp->type_.compare("knight") == 0)
        {
            return std::make_unique<Knight>(chesscontroller, entity);
        }
        else if (cp->type_.compare("bishop") == 0)
        {
            return std::make_unique<Bishop>(chesscontroller, entity);
        }
        else if (cp->type_.compare("rook") == 0)
        {
            return std::make_unique<Rook>(chesscontroller, entity);
        }
        else if (cp->type_.compare("queen") == 0)
        {
            return std::make_unique<Queen>(chesscontroller, entity);
        }
        else if (cp->type_.compare("king") == 0)
        {
            return std::make_unique<King>(chesscontroller, entity);
        }
        else
        {
            Logger::Log(logging::trivial::debug, log_location, "no movements found for " , entity->name);
            return std::make_unique<Movement>(chesscontroller, entity);
        }
    }   
};

#endif