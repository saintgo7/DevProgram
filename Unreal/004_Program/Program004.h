// Character
// Program 004

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program004.generated.h"

UCLASS()
class AProgram004 : public AActor
{
    GENERATED_BODY()

public:
    AProgram004();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
