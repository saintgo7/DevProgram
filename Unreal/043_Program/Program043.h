// Take Damage
// Program 043

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program043.generated.h"

UCLASS()
class AProgram043 : public AActor
{
    GENERATED_BODY()

public:
    AProgram043();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
