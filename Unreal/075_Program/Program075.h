// Particle Spawn
// Program 075

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program075.generated.h"

UCLASS()
class AProgram075 : public AActor
{
    GENERATED_BODY()

public:
    AProgram075();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
