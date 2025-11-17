// Particle System
// Program 071

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program071.generated.h"

UCLASS()
class AProgram071 : public AActor
{
    GENERATED_BODY()

public:
    AProgram071();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
