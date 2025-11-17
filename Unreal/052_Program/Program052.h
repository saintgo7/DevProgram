// Game State
// Program 052

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program052.generated.h"

UCLASS()
class AProgram052 : public AActor
{
    GENERATED_BODY()

public:
    AProgram052();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
