// Player Controller
// Program 005

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program005.generated.h"

UCLASS()
class AProgram005 : public AActor
{
    GENERATED_BODY()

public:
    AProgram005();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
