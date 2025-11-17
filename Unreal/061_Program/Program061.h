// Physics
// Program 061

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program061.generated.h"

UCLASS()
class AProgram061 : public AActor
{
    GENERATED_BODY()

public:
    AProgram061();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
