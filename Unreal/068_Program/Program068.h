// Material Parameter
// Program 068

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program068.generated.h"

UCLASS()
class AProgram068 : public AActor
{
    GENERATED_BODY()

public:
    AProgram068();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
